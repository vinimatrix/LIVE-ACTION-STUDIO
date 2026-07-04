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
