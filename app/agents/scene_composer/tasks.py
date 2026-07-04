from celery import Celery
from app.core.config import settings
from app.agents.scene_composer.scene_composer import SceneComposerAgent

celery_app = Celery(
    "scene_composer",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

scene_composer_agent = SceneComposerAgent()


@celery_app.task
def compose_scenes(analysis_data: dict):
    manga_analysis = analysis_data.get("manga_analysis", {})
    max_scenes = analysis_data.get("max_scenes", 5)
    result = scene_composer_agent.compose(manga_analysis, max_scenes)
    return result
