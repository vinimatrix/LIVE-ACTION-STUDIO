from celery import Celery
from app.core.config import settings
from app.agents.flow_prompt_builder.flow_prompt_builder import FlowPromptBuilderAgent

celery_app = Celery(
    "flow_prompt_builder",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

flow_prompt_builder_agent = FlowPromptBuilderAgent()


@celery_app.task
def build_flow_prompts(prompt_data: dict):
    scenes = prompt_data.get("scenes", [])
    character_mapping = prompt_data.get("character_mapping", {})
    result = flow_prompt_builder_agent.build_prompts(scenes, character_mapping)
    return result
