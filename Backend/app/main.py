from fastapi import FastAPI
from app.config import settings

from app.api import meetings

app = FastAPI(title=settings.APP_NAME)

app.include_router(meetings.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
