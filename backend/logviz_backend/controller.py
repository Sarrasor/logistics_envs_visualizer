import datetime
from io import BytesIO
import json
import logging
import pathlib
import threading
import uuid
from typing import Annotated, Callable, Union

import namesgenerator
from fastapi import File, Form, HTTPException, WebSocket, WebSocketDisconnect

from logviz_backend.runner import Runner
from logviz_backend.schema import (
    Healthcheck,
    HealthcheckStatus,
    RenderRequest,
    RenderResponse,
    RenderStatus,
    RunStatus,
)

logger = logging.getLogger("logviz_backend.controller")


class LogvizController:
    def __init__(self, runs_folder: str):
        self._runs_folder = pathlib.Path(runs_folder)
        self._runs_folder.mkdir(parents=True, exist_ok=True)
        self._runs_cache = {}

        self._runner = Runner()

        self._websockets: list[WebSocket] = []

        for run_folder in self._runs_folder.glob("*"):
            if not run_folder.is_dir():
                continue
            run_meta = run_folder / "meta.json"
            if not run_meta.exists():
                continue

            with open(run_meta, "r") as file:
                meta_data = json.load(file)
                meta_data["status"] = RunStatus[meta_data["status"]]

            self._add_cache_entry(meta_data)

    def _add_cache_entry(self, run_meta: dict) -> None:
        self._runs_cache[run_meta["id"]] = {
            "name": run_meta["name"],
            "creation_time": run_meta["creation_time"],
            "status": run_meta["status"],
            "message": run_meta["message"],
        }

    async def healthcheck(self) -> Healthcheck:
        return Healthcheck(status=HealthcheckStatus.UP)

    async def render(self, render_request: RenderRequest) -> RenderResponse:
        logger.info(
            f"Received render request id: {render_request.info.simulation_id} time: {render_request.observation.current_time}"
        )
        for websocket in self._websockets:
            await websocket.send_json(render_request.model_dump())

        return RenderResponse(status=RenderStatus.OK)

    async def websocket(self, websocket: WebSocket):
        await websocket.accept()
        self._websockets.append(websocket)
        logger.info("Websocket connected")

        try:
            while True:
                data = await websocket.receive_text()
                logger.info(f"Received websocket data: {data}")
        except WebSocketDisconnect:
            self._websockets.remove(websocket)
            logger.info("Websocket disconnected")

    def get_list_of_all_runs(self) -> list:
        logger.info("Request to get list of all runs")
        runs = []
        for run_id, run_preview_data in self._runs_cache.items():
            runs.append(
                {
                    "id": run_id,
                    "name": run_preview_data["name"],
                    "creation_time": run_preview_data["creation_time"],
                    "status": run_preview_data["status"],
                    "message": run_preview_data["message"],
                }
            )
        return runs

    def get_run_report(self, run_id: str) -> dict:
        logging.info(f"Request run id: '{run_id}'")
        if run_id not in self._runs_cache:
            raise HTTPException(status_code=404, detail=f"Run with id {run_id} was not found")

        run_folder = self._runs_folder / run_id
        run_report_path = run_folder / "run_report.json"

        with open(run_folder / "meta.json", "r") as file:
            run_meta = json.load(file)
            run_meta["status"] = RunStatus[run_meta["status"]]

        if run_report_path.exists():
            with open(run_report_path, "r") as file:
                run_report = json.load(file)
        else:
            run_report = {"orders": [], "workers": [], "metrics": []}

        report = run_report
        report["id"] = run_id
        report["description"] = {
            "name": run_meta["name"],
            "creation_time": run_meta["creation_time"],
            "status": run_meta["status"],
            "message": run_meta["message"],
            "logistics_environment": run_meta["parameters"]["logistics_environment"],
            "location_mode": run_meta["parameters"]["location_mode"],
            "run_mode": run_meta["parameters"]["run_mode"],
        }

        return report

    def _get_asynchronous_solving_function(
        self,
        input_file: bytes,
        run_folder: pathlib.Path,
    ) -> Callable[[], None]:
        def solve() -> None:
            with open(run_folder / "meta.json", "r") as file:
                run_meta = json.load(file)

            try:
                input_file_data = BytesIO(input_file)

                input_file_path = run_folder / "input_file.xlsx"
                with open(input_file_path, "wb") as file:
                    file.write(input_file_data.getbuffer())

                run_meta["status"] = RunStatus.RUNNING
                run_meta["message"] = ""
                self._update_meta(run_meta, run_folder)

                self._runner.run(input_file_data, run_meta, run_folder)

                run_meta["status"] = RunStatus.COMPLETED
                run_meta["message"] = ""
            except Exception as e:
                failed_message = f"Failed to run: {e}"
                logger.warning(failed_message)
                run_meta["status"] = RunStatus.ERROR
                run_meta["message"] = failed_message

            self._update_meta(run_meta, run_folder)

        return solve

    async def solve(
        self,
        input_file: Annotated[bytes, File()],
        logistics_environment: Annotated[str, Form()],
        location_mode: Annotated[str, Form()],
        run_mode: Annotated[str, Form()],
        run_name: Union[str, None] = Form(default=None),
    ) -> dict:
        logger.info(f"Received solve request for run: {run_name}")

        run_id = str(uuid.uuid4())

        if not run_name:
            run_name = namesgenerator.get_random_name()

        try:
            creation_time = datetime.datetime.now().isoformat()
            run_meta = {
                "id": run_id,
                "name": run_name,
                "creation_time": creation_time,
                "status": RunStatus.CREATED,
                "message": "",
                "parameters": {
                    "logistics_environment": logistics_environment,
                    "location_mode": location_mode,
                    "run_mode": run_mode,
                },
            }

            run_folder = self._runs_folder / run_id
            run_folder.mkdir(parents=True)
            self._update_meta(run_meta, run_folder)

            thread = threading.Thread(
                target=self._get_asynchronous_solving_function(input_file, run_folder),
                daemon=True,
            )
            thread.start()
            status = {"status": RunStatus.CREATED, "message": "ok", "run_id": run_id}
        except Exception as e:
            failed_message = f"Failed to create run {run_id}: {e}"
            logger.warning(failed_message)
            status = {
                "status": RunStatus.ERROR,
                "message": failed_message,
                "run_id": run_id,
            }

        return status

    def _update_meta(self, run_meta: dict, run_folder: pathlib.Path) -> None:
        with open(run_folder / "meta.json", "w") as file:
            json.dump(run_meta, file, indent=4)
        self._add_cache_entry(run_meta)
