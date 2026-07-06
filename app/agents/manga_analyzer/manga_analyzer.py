from typing import Dict, Any
import json
import urllib.request

class MangaAnalyzerAgent:
    def __init__(self):
        self.ollama_url = "http://127.0.0.1:11434/api/generate"
        self.model = "gemma4:latest"

    def analyze(self, image_base64: str, filename: str = "") -> Dict[str, Any]:
        system_prompt = """Eres un experto analista de manga. Analiza la imagen de manga proporcionada y extrae:
- characters: lista de personajes (name, appearance, expression, position)
- setting: descripción del escenario
- action: acción principal
- dialogue: diálogos visibles (traducidos y adaptados a español latino neutro si provienen de español de España u otros idiomas)
- mood: atmósfera/estado de ánimo
- panels: estructura de paneles

Responde SOLO con JSON válido, sin markdown ni explicaciones."""

        payload = {
            "model": self.model,
            "prompt": f"{system_prompt}\n\nAnaliza esta página de manga:",
            "images": [image_base64],
            "stream": False,
            "options": {"temperature": 0.1}
        }

        try:
            data = json.dumps(payload).encode()
            req = urllib.request.Request(
                self.ollama_url, data=data,
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=300) as resp:
                result = json.loads(resp.read())
                response_text = result.get("response", "{}")
                return json.loads(response_text)
        except Exception as e:
            return {"error": str(e), "characters": [], "setting": "", "action": "", "dialogue": [], "mood": "", "panels": []}
