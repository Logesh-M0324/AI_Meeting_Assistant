from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    APP_NAME: str = "AI Meeting Assistant"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str

    # Redis / Celery
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = REDIS_URL
    CELERY_RESULT_BACKEND: str = REDIS_URL

    # LLM
    GROQ_API_KEY: str | None = None

    # Email (Outlook)
    OUTLOOK_EMAIL: str | None = None
    OUTLOOK_PASSWORD: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
