from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from container import ApplicationContainer
from typing import Any

from infrastructure.api import AccountController

def Setup(app: FastAPI, container: ApplicationContainer) -> None:

    #Controllers
    app.include_router(AccountController.router)

    #Inject Dependencies
    container.wire(
        modules=[
            AccountController,
        ]
    )

    # Customize the openAPI documentation
    def CustomOpenApi() -> Any:
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Music Sharing App",
            # version=__version__,
            version="0.0.1",
            description="My music sharing app API'",
            routes=app.routes,
        )
        if not container.configuration.api_prefix():
            openapi_schema["servers"] = [{"url": "/"}]
        else:
            openapi_schema["servers"] = [{"url": container.configuration.api_prefix()}]
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = CustomOpenApi