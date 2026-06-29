import pytest
from app.agents.prompt_builder.prompt_builder import PromptBuilderAgent


def test_prompt_builder_initialization():
    agent = PromptBuilderAgent()
    assert agent is not None


def test_build_image_prompt():
    agent = PromptBuilderAgent()
    scene_data = {
        "description": "A hero stands on a cliff overlooking the ocean",
        "duration": 8.0,
        "character_data": {
            "Hero": {
                "personality_traits": ["brave", "determined"],
                "expressions": ["determined"]
            }
        },
        "environment_data": {
            "location_type": "ocean_cliff",
            "lighting_conditions": {"time_of_day": "sunset", "weather": "clear"}
        },
        "camera_notes": {
            "shot_type": "wide",
            "movement": "static"
        }
    }

    prompt = agent.build_image_prompt(scene_data)

    assert "cinematic scene" in prompt
    assert "hero stands on a cliff" in prompt.lower()
    assert "brave, determined" in prompt
    assert "sunset" in prompt
    assert "wide, static" in prompt


def test_build_video_prompt():
    agent = PromptBuilderAgent()
    image_prompt = "A beautiful landscape"
    video_prompt = agent.build_video_prompt(image_prompt, 6.0)

    assert "beautiful landscape" in video_prompt
    assert "smooth motion over 6.0 seconds" in video_prompt
    assert "cinematic video" in video_prompt


def test_build_voice_prompt():
    agent = PromptBuilderAgent()
    dialogue = {
        "character": "Wizard",
        "text": "By the power of light!",
        "emotion": "excited"
    }

    prompt = agent.build_voice_prompt(dialogue)
    assert "Wizard speaking with excited emotion:" in prompt
    assert "By the power of light!" in prompt


def test_build_music_prompt():
    agent = PromptBuilderAgent()
    assert "brief ambient" in agent.build_music_prompt({"duration": 3.0})
    assert "dramatic tension" in agent.build_music_prompt({"duration": 7.0})
    assert "epic orchestral" in agent.build_music_prompt({"duration": 12.0})


def test_build_effects_prompt():
    agent = PromptBuilderAgent()
    assert "explosion and fire effects" in agent.build_effects_prompt(
        {"actions": ["Character triggers an explosion"]}
    )
    assert "magical particle effects" in agent.build_effects_prompt(
        {"actions": ["Wizard casts a spell"]}
    )
    assert "subtle environmental effects" in agent.build_effects_prompt(
        {"actions": ["Character walks"]}
    )
