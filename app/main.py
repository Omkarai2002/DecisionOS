from fastapi import FastAPI

from app.api.routes.negotiation import router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(router)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "app": settings.APP_NAME
    }