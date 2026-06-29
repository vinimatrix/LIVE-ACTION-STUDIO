from celery import Celery
from app.core.config import settings
from app.agents.editor.editor import EditorAgent

celery_app = Celery(
    "editor",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

editor_agent = EditorAgent()


@celery_app.task
def assemble_final_video(editor_data: dict):
    result = editor_agent.assemble_video(
        video_clip=editor_data.get("video_clip"),
        audio_tracks=editor_data.get("audio_tracks", []),
        effect_layers=editor_data.get("effect_layers", []),
        music_track=editor_data.get("music_track"),
        subtitle_data=editor_data.get("subtitle_data")
    )
    return result
