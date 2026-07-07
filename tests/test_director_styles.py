import pytest
from app.agents.director_styles import DIRECTOR_STYLES, STYLE_MOOD_MAP, resolve_style

REQUIRED_KEYS = [
    "action_moods", "preferred_movements", "preferred_shot_types",
    "slow_motion", "shot_duration_range", "color_grading", "lighting_contrast"
]


class TestDirectorStyles:
    def test_all_presets_have_required_keys(self):
        for name, preset in DIRECTOR_STYLES.items():
            for key in REQUIRED_KEYS:
                assert key in preset, f"{name} missing key: {key}"

    def test_six_directors_defined(self):
        assert set(DIRECTOR_STYLES.keys()) == {
            "michael_bay", "russo_brothers", "sam_raimi",
            "christopher_nolan", "akira_kurosawa", "james_gunn"
        }

    def test_each_preset_has_at_least_one_movement(self):
        for name, preset in DIRECTOR_STYLES.items():
            assert len(preset["preferred_movements"]) > 0

    def test_each_preset_has_at_least_one_shot_type(self):
        for name, preset in DIRECTOR_STYLES.items():
            assert len(preset["preferred_shot_types"]) > 0

    def test_slow_motion_has_enabled_flag(self):
        for name, preset in DIRECTOR_STYLES.items():
            assert "enabled" in preset["slow_motion"]

    def test_shot_duration_range_is_tuple_of_two(self):
        for name, preset in DIRECTOR_STYLES.items():
            lo, hi = preset["shot_duration_range"]
            assert lo <= hi


class TestStyleMoodMap:
    def test_resolve_style_manual_override(self):
        assert resolve_style("michael_bay") == "michael_bay"

    def test_resolve_style_by_mood(self):
        assert resolve_style(mood="explosive") == "michael_bay"
        assert resolve_style(mood="intense") == "russo_brothers"
        assert resolve_style(mood="epic") == "akira_kurosawa"

    def test_resolve_style_none_for_unknown_mood(self):
        assert resolve_style(mood="unknown_xyz") is None

    def test_resolve_style_override_beats_mood(self):
        assert resolve_style("james_gunn", mood="explosive") == "james_gunn"

    def test_resolve_style_invalid_name_falls_back_to_mood(self):
        result = resolve_style("nonexistent_style", mood="explosive")
        assert result == "michael_bay"

    def test_resolve_style_invalid_name_and_unknown_mood(self):
        assert resolve_style("nonexistent_style", mood="xyz") is None

    def test_resolve_style_empty_mood(self):
        assert resolve_style(mood="") is None
