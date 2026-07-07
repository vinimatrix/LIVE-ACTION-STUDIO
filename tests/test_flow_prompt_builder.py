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


class TestFlowPromptBuilderFmtTime:
    def test_fmt_time_zero(self):
        agent = FlowPromptBuilderAgent()
        assert agent._fmt_time(0) == "00:00"

    def test_fmt_time_seconds_only(self):
        agent = FlowPromptBuilderAgent()
        assert agent._fmt_time(45) == "00:45"

    def test_fmt_time_one_minute(self):
        agent = FlowPromptBuilderAgent()
        assert agent._fmt_time(60) == "01:00"

    def test_fmt_time_minutes_and_seconds(self):
        agent = FlowPromptBuilderAgent()
        assert agent._fmt_time(125) == "02:05"

    def test_fmt_time_hour_boundary(self):
        agent = FlowPromptBuilderAgent()
        assert agent._fmt_time(3600) == "60:00"

    def test_fmt_time_large_value(self):
        agent = FlowPromptBuilderAgent()
        assert agent._fmt_time(7384) == "123:04"

    def test_fmt_time_float_seconds(self):
        agent = FlowPromptBuilderAgent()
        assert agent._fmt_time(90.7) == "01:30"

    def test_fmt_time_just_under_minute(self):
        agent = FlowPromptBuilderAgent()
        assert agent._fmt_time(59) == "00:59"

    def test_fmt_time_exact_59_59(self):
        agent = FlowPromptBuilderAgent()
        assert agent._fmt_time(3599) == "59:59"

    def test_fmt_time_negative(self):
        agent = FlowPromptBuilderAgent()
        assert agent._fmt_time(-5) == "-1:55"


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


class TestFlowPromptBuilderDirector:
    SAMPLE_SCENES = [
        {
            "scene_id": 1,
            "duration": 8.0,
            "characters": [
                {"name": "Goku", "appearance": "orange gi", "expression": "determined", "position": "center"},
            ],
            "description": "Goku charges at Freezer with explosion",
            "camera": {"shot_type": "low_angle", "movement": "360_orbit", "lens": "35mm f/2.8"},
            "lighting": {"time_of_day": "sunset", "mood_lighting": "explosive"},
            "dialogue": [{"character": "Goku", "text": "Freezer!"}],
            "transition": "cut",
            "director_style": "michael_bay",
        }
    ]
    CHARACTER_MAPPING = {"Goku": "personaje_1"}

    def test_build_prompts_includes_director_section(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING, director_style="michael_bay")
        prompt_text = prompts[0]["prompt_text"]
        assert "DIRECCIÓN" in prompt_text

    def test_build_prompts_includes_style_name(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING, director_style="michael_bay")
        prompt_text = prompts[0]["prompt_text"]
        assert "Michael Bay" in prompt_text

    def test_build_prompts_no_style_no_director_section(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING)
        prompt_text = prompts[0]["prompt_text"]
        assert "DIRECCIÓN" not in prompt_text

    def test_build_prompts_falls_back_to_mood_style(self):
        agent = FlowPromptBuilderAgent()
        prompts = agent.build_prompts(self.SAMPLE_SCENES, self.CHARACTER_MAPPING)
        prompt_text = prompts[0]["prompt_text"]
        assert "DIRECCIÓN" not in prompt_text
