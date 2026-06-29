from pydantic import BaseSettings

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AI Live Action Studio"

    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/ai_studio"

    # Redis/Celery
    REDIS_URL: str = "redis://localhost:6379/0"

    # MinIO/S3
    MINIO_ENDPOINT: str = "localhost:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    MINIO_BUCKET: str = "ai-studio-assets"

    # Ollama
    OLLAMA_BASE_URL: str = "http://localhost:11434"

    class Config:
        case_sensitive = True

settings = Settings()