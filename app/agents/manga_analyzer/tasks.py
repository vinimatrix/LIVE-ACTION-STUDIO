from celery import Celery
from app.core.config import settings
from app.agents.manga_analyzer.manga_analyzer import MangaAnalyzerAgent

celery_app = Celery(
    "manga_analyzer",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

manga_analyzer_agent = MangaAnalyzerAgent()


@celery_app.task
def analyze_manga_page(manga_data: dict):
    image = manga_data.get("image")
    filename = manga_data.get("filename", "")
    result = manga_analyzer_agent.analyze(image, filename)
    return result
