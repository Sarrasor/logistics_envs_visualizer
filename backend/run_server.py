import logging

import uvicorn
from fastapi import FastAPI, APIRouter

from logviz_backend.schema import (
    Healthcheck,
    RenderResponse,
    RunReport,
    RunThumbnail,
    SolveResponse,
)
from logviz_backend.controller import LogvizController


def main():
    runs_folder = "server_data/runs"
    logging_level = logging.INFO
    logging.basicConfig(level=logging_level)

    controller = LogvizController(runs_folder=runs_folder)
    app = FastAPI()

    router = APIRouter()
    router.add_api_route(
        "/healthcheck",
        controller.healthcheck,
        response_model=Healthcheck,
        methods=["GET"],
    )
    router.add_api_route(
        "/render",
        controller.render,
        response_model=RenderResponse,
        methods=["POST"],
    )
    router.add_api_route(
        "/runs",
        controller.get_list_of_all_runs,
        response_model=list[RunThumbnail],
        methods=["GET"],
    )
    router.add_api_route(
        "/runs/{run_id}",
        controller.get_run_report,
        response_model=RunReport,
        methods=["GET"],
    )
    router.add_api_route(
        "/solve",
        controller.solve,
        response_model=SolveResponse,
        methods=["POST"],
    )

    router.add_api_websocket_route("/ws", controller.websocket)

    app.include_router(router)
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level=logging_level)
    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    main()
