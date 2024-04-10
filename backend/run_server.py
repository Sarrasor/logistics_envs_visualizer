import logging

import uvicorn
from fastapi import FastAPI, APIRouter

from logviz_backend.schema import Healthcheck, RenderResponse
from logviz_backend.controller import LogvizController


def main():
    logging_level = logging.INFO
    logging.basicConfig(level=logging_level)
    controller = LogvizController()
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
    router.add_api_websocket_route("/ws", controller.websocket)

    app.include_router(router)
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level=logging_level)
    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    main()
