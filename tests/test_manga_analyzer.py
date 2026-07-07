import pytest
import json
from app.agents.manga_analyzer.manga_analyzer import MangaAnalyzerAgent

class TestMangaAnalyzer:
    def test_analyze_returns_expected_keys(self, mocker):
        mock_response = {
            "characters": [{"name": "Goku", "appearance": "orange gi, spiky black hair", "expression": "angry", "position": "center"}],
            "setting": "A rocky planet with red sky, two suns in background",
            "action": "Goku powering up, yelling, aura of light around him",
            "dialogue": ["AHHHHHHHHH!"],
            "mood": "epic, tense, battle climax",
            "panels": [{"panel_number": 1, "description": "Full page spread of Goku powering up"}]
        }
        mock = mocker.patch('urllib.request.urlopen')
        mock.return_value.read.return_value = json.dumps({"response": json.dumps(mock_response)}).encode()

        agent = MangaAnalyzerAgent()
        result = agent.analyze("fake_base64", "test.png")

        assert "characters" in result
        assert "setting" in result
        assert "action" in result
        assert "dialogue" in result
        assert "mood" in result
        assert "panels" in result
        assert isinstance(result["characters"], list)

    def test_analyze_with_empty_image(self, mocker):
        mocker.patch('urllib.request.urlopen').side_effect = Exception("Ollama error")
        agent = MangaAnalyzerAgent()
        result = agent.analyze("", "test.png")
        assert "error" in result

    def test_gemini_backend_returns_expected_keys(self, mocker):
        mock_response = {
            "characters": [{"name": "Naruto", "appearance": "rubio, chaqueta naranja", "expression": "sonriendo", "position": "centro"}],
            "setting": "Aldea Oculta de la Hoja al atardecer",
            "action": "Naruto saludando con la mano",
            "dialogue": ["¡Voy a ser Hokage!"],
            "mood": "alegre, inspirador",
            "panels": [{"panel_number": 1, "description": "Naruto de pie sobre el monumento Hokage"}]
        }
        mock_client = mocker.patch('google.genai.Client')
        mock_instance = mock_client.return_value
        mock_instance.models.generate_content.return_value.text = json.dumps(mock_response)

        agent = MangaAnalyzerAgent(backend="gemini")
        result = agent.analyze("fake_base64", "naruto.png")

        assert "characters" in result
        assert "setting" in result
        assert "action" in result
        assert "dialogue" in result
        assert "mood" in result
        assert "panels" in result
        assert isinstance(result["characters"], list)

    def test_gemini_backend_fallback_on_error(self, mocker):
        mocker.patch('google.genai.Client').side_effect = Exception("Gemini API error")
        agent = MangaAnalyzerAgent(backend="gemini")
        result = agent.analyze("", "test.png")
        assert "error" in result


from app.agents.manga_analyzer.manga_analyzer import (
    _hint_characters, _intelligent_fallback, SERIES_CHARACTERS, FALLBACK_NAMES
)


class TestMangaAnalyzerInternalMethods:
    def test_hint_characters_known_series_by_name(self):
        result = _hint_characters("", manga_series="boruto")
        assert result == SERIES_CHARACTERS["boruto"]

    def test_hint_characters_known_series_case_insensitive(self):
        result = _hint_characters("", manga_series="NARUTO")
        assert result == SERIES_CHARACTERS["naruto"]

    def test_hint_characters_known_series_from_filename(self):
        result = _hint_characters("one_piece_chapter_1.png")
        assert result == SERIES_CHARACTERS["one_piece"]

    def test_hint_characters_unknown_series_returns_empty(self):
        result = _hint_characters("", manga_series="unknown_series")
        assert result == []

    def test_hint_characters_empty_inputs(self):
        result = _hint_characters("", manga_series="")
        assert result == []

    def test_hint_characters_filename_with_special_chars(self):
        result = _hint_characters("dragon-ball-001.jpg")
        assert result == SERIES_CHARACTERS["dragon_ball"]

    def test_hint_characters_filename_with_spaces(self):
        result = _hint_characters("demon slayer page 3.png")
        assert result == SERIES_CHARACTERS["demon_slayer"]

    def test_extract_json_raw_json(self):
        agent = MangaAnalyzerAgent()
        raw = '{"characters": [{"name": "Goku"}], "mood": "epic"}'
        result = agent._extract_json(raw)
        assert result["mood"] == "epic"
        assert result["characters"][0]["name"] == "Goku"

    def test_extract_json_with_markdown_fence(self):
        agent = MangaAnalyzerAgent()
        raw = '```json\n{"characters": [{"name": "Naruto"}]}\n```'
        result = agent._extract_json(raw)
        assert result["characters"][0]["name"] == "Naruto"

    def test_extract_json_with_markdown_fence_no_lang(self):
        agent = MangaAnalyzerAgent()
        raw = '```\n{"action": "fighting"}\n```'
        result = agent._extract_json(raw)
        assert result["action"] == "fighting"

    def test_extract_json_with_extra_whitespace(self):
        agent = MangaAnalyzerAgent()
        raw = '  \n  {"test": "value"}  \n'
        result = agent._extract_json(raw)
        assert result["test"] == "value"

    def test_intelligent_fallback_returns_required_keys(self):
        result = _intelligent_fallback("test.png", "naruto")
        assert "characters" in result
        assert "setting" in result
        assert "action" in result
        assert "dialogue" in result
        assert "mood" in result
        assert "panels" in result

    def test_intelligent_fallback_known_series_uses_known_characters(self):
        result = _intelligent_fallback("naruto_chapter_1.png")
        for char in result["characters"]:
            assert char["name"] in SERIES_CHARACTERS["naruto"]

    def test_intelligent_fallback_unknown_series_uses_fallback_names(self):
        result = _intelligent_fallback("unknown_manga_001.png")
        for char in result["characters"]:
            assert char["name"] in FALLBACK_NAMES

    def test_intelligent_fallback_deterministic_output(self):
        r1 = _intelligent_fallback("test.png")
        r2 = _intelligent_fallback("test.png")
        assert r1 == r2

    def test_intelligent_fallback_different_filenames_can_differ(self):
        r1 = _intelligent_fallback("naruto_chapter_1.png")
        r2 = _intelligent_fallback("boruto_chapter_1.png")
        known_chars_naruto = set(c["name"] for c in r1["characters"])
        known_chars_boruto = set(c["name"] for c in r2["characters"])
        assert known_chars_naruto != known_chars_boruto

    def test_intelligent_fallback_returns_list_of_panels(self):
        result = _intelligent_fallback("test.png")
        assert len(result["panels"]) == 3

    def test_intelligent_fallback_limited_to_4_characters(self):
        result = _intelligent_fallback("boruto_special.png")
        assert len(result["characters"]) <= 4
