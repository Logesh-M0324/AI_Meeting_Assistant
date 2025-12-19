from Backend.core.celery_app import Celery
from app.config import settings

celery_app = Celery(
    "ai_meeting_assistant",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

# Auto-discover tasks from workers package
celery_app.autodiscover_tasks(["app.workers"])
