import logging
from typing import Optional
from fastapi import WebSocket, WebSocketDisconnect

from logviz_backend.schema import (
    Healthcheck,
    HealthcheckStatus,
    RenderRequest,
    RenderResponse,
    RenderStatus,
)

logger = logging.getLogger("logviz_backend.controller")


class LogvizController:
    def __init__(self):
        self._websockets: list[WebSocket] = []

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
