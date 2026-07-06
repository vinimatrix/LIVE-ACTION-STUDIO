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


from app.agents.storyboard.storyboard import StoryboardAgent

class TestFlowPromptBuilderStoryboard:
    SAMPLE_SCENES = [
        {
            "scene_id": 1,
            "duration": 7.0,
            "characters": [
                {"name": "Goku", "appearance": "orange gi, spiky black hair",
                 "expression": "angry", "position": "left"},
                {"name": "Freezer", "appearance": "white armor",
                 "expression": "smirking", "position": "right"}
            ],
            "description": "Goku confronts Freezer on the battlefield",
            "camera": {"shot_type": "wide", "movement": "static", "lens": "24mm f/4"},
            "lighting": {"time_of_day": "day", "mood_lighting": "tense"},
            "dialogue": [
                {"character": "Goku", "text": "Freezer!"},
                {"character": "Freezer", "text": "Foolish Saiyan."}
            ],
            "transition": "cut"
        }
    ]
    CHARACTER_MAPPING = {"Goku": "personaje_1", "Freezer": "personaje_2"}

    def test_build_storyboard_prompts_returns_list(self):
        agent = FlowPromptBuilderAgent()
        storyboard_agent = StoryboardAgent()
        prompts = agent.build_storyboard_prompts(
            self.SAMPLE_SCENES, self.CHARACTER_MAPPING, storyboard_agent
        )
        assert isinstance(prompts, list)
        assert len(prompts) == 1

    def test_storyboard_prompt_contains_global_context(self):
        agent = FlowPromptBuilderAgent()
        storyboard_agent = StoryboardAgent()
        prompts = agent.build_storyboard_prompts(
            self.SAMPLE_SCENES, self.CHARACTER_MAPPING, storyboard_agent
        )
        prompt_text = prompts[0]["prompt_text"]
        assert "ESCENA 1" in prompt_text
        assert "Contexto Global" in prompt_text
        assert "SHOT 1" in prompt_text

    def test_storyboard_prompt_contains_per_shot_sections(self):
        agent = FlowPromptBuilderAgent()
        storyboard_agent = StoryboardAgent()
        prompts = agent.build_storyboard_prompts(
            self.SAMPLE_SCENES, self.CHARACTER_MAPPING, storyboard_agent
        )
        prompt_text = prompts[0]["prompt_text"]
        for shot_num in (1, 2):
            assert f"SHOT {shot_num}" in prompt_text
            assert "TIPO:" in prompt_text
            assert "MOV:" in prompt_text

    def test_storyboard_prompt_has_character_mapping(self):
        agent = FlowPromptBuilderAgent()
        storyboard_agent = StoryboardAgent()
        prompts = agent.build_storyboard_prompts(
            self.SAMPLE_SCENES, self.CHARACTER_MAPPING, storyboard_agent
        )
        prompt_text = prompts[0]["prompt_text"]
        assert "personaje_1" in prompt_text
        assert "personaje_2" in prompt_text

    def test_storyboard_prompt_includes_anti_alucinacion(self):
        agent = FlowPromptBuilderAgent()
        storyboard_agent = StoryboardAgent()
        prompts = agent.build_storyboard_prompts(
            self.SAMPLE_SCENES, self.CHARACTER_MAPPING, storyboard_agent
        )
        prompt_text = prompts[0]["prompt_text"]
        assert "ANTI-ALUCINACIÓN" in prompt_text
