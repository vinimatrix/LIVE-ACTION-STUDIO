from pydantic_settings import BaseSettings, SettingsConfigDict

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

    # ComfyUI
    COMFYUI_URL: str = "http://127.0.0.1:8188"

    # Cloud AI
    GEMINI_API_KEY: str = ""
    MANGA_ANALYZER_BACKEND: str = "ollama"  # "ollama" | "gemini"
    GEMINI_VISION_MODEL: str = "gemini-2.5-flash"

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")

settings = Settings()