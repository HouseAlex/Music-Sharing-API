from fastapi import FastAPI, Path
import uvicorn

from container import ApplicationContainer
from infrastructure.api.setup import Setup

def init() -> FastAPI:
    container = ApplicationContainer()

    # Setup Logging
    
    # Init Database

    # Init API and attach the container
    app = FastAPI()
    app.extra["container"] = container

    # Do setup and dependencies wiring
    Setup(app, container)

    return app

def start() -> None:
    app = init()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )

if __name__ == "__main__":
    start()