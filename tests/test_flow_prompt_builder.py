import pytest
from app.agents.flow_prompt_builder.flow_prompt_builder import FlowPromptBuilderAgent

class TestFlowPromptBuilder:
    SAMPLE_SCENES = [
        {
            "scene_id": 1,
            "duration": 8.0,
            "characters": [
                {"name": "Goku", "appearance": "orange gi, spiky black hair",
                 "expression": "angry", "position": "center"}
            ],
            "description": "Goku powering up with golden aura",
            "camera": {"shot_type": "medium", "movement": "dolly", "lens": "35mm f/2.8"},
            "lighting": {"time_of_day": "sunset", "mood_lighting": "epic"},
            "dialogue": [{"character": "Goku", "text": "AHHHHHH!"}],
            "transition": "fade_in"
        }
    ]
    CHARACTER_MAPPING = {"Goku": "personaje_1", "Freezer": "personaje_2"}

    def test_build_prompts_returns_list(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING)
        assert isinstance(prompts, list)
        assert len(prompts) == 1

    def test_prompt_has_required_sections(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING)
        prompt_text = prompts[0]["prompt_text"]
        assert "PERSONAJES" in prompt_text
        assert "ESCENARIO" in prompt_text
        assert "CÁMARA" in prompt_text
        assert "ILUMINACIÓN" in prompt_text
        assert "MOOD" in prompt_text
        assert "ACCIÓN" in prompt_text
        assert "SPECS TÉCNICAS" in prompt_text
        assert "ANTI-ALUCINACIÓN" in prompt_text

    def test_prompt_contains_character_mapping(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING)
        prompt_text = prompts[0]["prompt_text"]
        assert "personaje_1" in prompt_text
        assert "Goku" in prompt_text

    def test_prompt_includes_duration_and_scene_number(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING)
        assert prompts[0]["scene_number"] == 1
        assert prompts[0]["duration"] == 8.0
