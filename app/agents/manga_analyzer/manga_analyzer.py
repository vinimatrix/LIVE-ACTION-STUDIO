from typing import Dict, Any, Optional
import json
import urllib.request
import hashlib
from app.core.config import settings

SERIES_CHARACTERS = {
    "boruto": ["Boruto Uzumaki", "Sarada Uchiha", "Shikamaru Nara", "Konohamaru Sarutobi", "Naruto Uzumaki", "Sasuke Uchiha", "Kawaki", "Mitsuki", "Himawari Uzumaki", "Hinata Uzumaki"],
    "naruto": ["Naruto Uzumaki", "Sasuke Uchiha", "Sakura Haruno", "Kakashi Hatake", "Hinata Hyuga", "Shikamaru Nara"],
    "one_piece": ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Sanji", "Tony Tony Chopper", "Nico Robin", "Franky", "Jimbei", "Brook"],
    "dragon_ball": ["Goku", "Vegeta", "Piccolo", "Gohan", "Freezer", "Trunks"],
    "demon_slayer": ["Tanjiro Kamado", "Nezuko Kamado", "Zenitsu Agatsuma", "Inosuke Hashibira", "Giyu Tomioka"],
}

FALLBACK_NAMES = ["Ryo", "Kenji", "Yuki", "Sakura", "Takeshi", "Akira", "Hana", "Kaito"]
FALLBACK_SETTINGS = [
    "Templo antiguo en la montaña al atardecer",
    "Callejón lluvioso en Neo-Tokio, luces de neón reflejándose en charcos",
    "Azotea de un rascacielos con vista a la ciudad distópica",
    "Interior de un laboratorio abandonado con pantallas rotas",
    "Bosque de bambú al amanecer con niebla baja",
    "Arena de batalla con escombros y humo de fondo",
    "Estación de tren vacía al anochecer",
    "Dōjō de kendo con luz tenue filtrándose por las ventanas",
]
FALLBACK_ACTIONS = [
    "Caminando lentamente entre la multitud con las manos en los bolsillos",
    "Empuñando una katana en posición de combate",
    "Mirando fijamente al horizonte con el viento moviendo su cabello",
    "Golpeando con un puñetazo directo al oponente",
    "Saltando entre edificios en persecución",
    "Sentado en meditación con los ojos cerrados",
    "Huyendo de una explosión mientras protege a alguien",
    "Sosteniendo un objeto misterioso que emite luz",
]
FALLBACK_MOODS = ["Suspenso", "Melancólico", "Épico", "Tenso", "Sereno", "Sombrío", "Energético", "Misterioso"]
FALLBACK_DIALOGUES = [
    ["No te detengas ahora.", "¡El destino del mundo está en juego!"],
    ["¿Crees que puedes vencerme?", "Lo haré, cueste lo que cueste."],
    ["Siempre supe que volverías.", "No hay otro lugar al que pertenezca."],
    ["Este es el final.", "No... esto es solo el comienzo."],
    ["Confía en mí.", "Ya no sé en quién confiar."],
    ["¡Protégela a toda costa!", "Lo juro por mi honor."],
]

SYSTEM_PROMPT = """Eres un experto analista de manga. Analiza la imagen de manga proporcionada y extrae:
- characters: lista de personajes (name, appearance, expression, position)
- setting: descripción del escenario
- action: acción principal
- dialogue: diálogos visibles TRADUCIDOS A ESPAÑOL LATINO NEUTRO. Traduce TODOS los textos del manga (japonés, inglés, etc.) al español latino neutro. No conserves texto en otros idiomas.
- mood: atmósfera/estado de ánimo
- panels: lista de paneles en ORDEN DE LECTURA (de derecha a izquierda, de arriba abajo)

REGLAS DE ORDEN DE LECTURA (CRÍTICO PARA PANELES):
- El manga se lee de derecha a izquierda y de arriba abajo
- Si hay 2 paneles pequeños a la derecha y 1 grande a la izquierda, el orden es: panel superior derecho → panel inferior derecho → panel grande izquierdo
- Si hay 1 panel grande a la derecha y 2 pequeños a la izquierda, el orden es: panel grande derecho → panel superior izquierdo → panel inferior izquierdo
- Los paneles deben listarse ESTRICTAMENTE en el orden narrativo correcto

Responde SOLO con JSON válido, sin markdown ni explicaciones."""


def _hint_characters(filename: str, manga_series: str = "") -> list:
    if manga_series:
        lower = manga_series.lower().strip()
        for series, chars in SERIES_CHARACTERS.items():
            norm_series = series.replace("_", " ").replace("-", " ")
            if norm_series in lower or lower in norm_series:
                return chars
    lower = filename.lower().replace("_", " ").replace("-", " ").replace(".", " ")
    for series, chars in SERIES_CHARACTERS.items():
        norm_series = series.replace("_", " ").replace("-", " ")
        if norm_series in lower:
            return chars
    return []


def _intelligent_fallback(filename: str, manga_series: str = "") -> Dict[str, Any]:
    h = int(hashlib.md5(filename.encode()).hexdigest(), 16)
    idx = h % 1000
    n = len(FALLBACK_NAMES)

    known = _hint_characters(filename, manga_series)
    if known:
        char_list = []
        for i, name in enumerate(known[:4]):
            char_list.append({
                "name": name,
                "appearance": "Personaje del universo manga reconocible",
                "expression": "Serio",
                "position": f"Plano {'central' if i == 0 else 'secundario'}",
            })
        setting = FALLBACK_SETTINGS[idx % len(FALLBACK_SETTINGS)]
    else:
        char1 = FALLBACK_NAMES[idx % n]
        char2 = FALLBACK_NAMES[(idx + 3) % n]
        char_list = [
            {
                "name": char1,
                "appearance": "Cabello oscuro, mirada seria, cicatriz en la ceja izquierda",
                "expression": "Determinado",
                "position": "Primer plano, ligeramente a la izquierda",
            },
            {
                "name": char2,
                "appearance": "Cabello claro, complexión delgada, viste uniforme escolar",
                "expression": "Sorprendido",
                "position": "Segundo plano a la derecha",
            },
        ]
        setting = FALLBACK_SETTINGS[idx % len(FALLBACK_SETTINGS)]

    action = FALLBACK_ACTIONS[idx % len(FALLBACK_ACTIONS)]
    mood = FALLBACK_MOODS[idx % len(FALLBACK_MOODS)]
    dialogue = FALLBACK_DIALOGUES[idx % len(FALLBACK_DIALOGUES)]

    return {
        "characters": char_list,
        "setting": setting,
        "action": action,
        "dialogue": dialogue,
        "mood": mood,
        "panels": [
            {"panel": 1, "description": "Vista general del escenario"},
            {"panel": 2, "description": f"Acercamiento a {char_list[0]['name']} con expresión de {mood.lower()}"},
            {"panel": 3, "description": f"Interacción entre personajes"},
        ],
    }


class MangaAnalyzerAgent:
    def __init__(self, backend: Optional[str] = None):
        self.backend = (backend or settings.MANGA_ANALYZER_BACKEND).lower()
        self.ollama_url = f"{settings.OLLAMA_BASE_URL}/api/generate"
        self.ollama_model = "gemma4:latest"
        self.gemini_model = settings.GEMINI_VISION_MODEL
        self.gemini_api_key = settings.GEMINI_API_KEY
        self.manga_series = ""

    def _analyze_ollama(self, image_base64: str, filename: str) -> Dict[str, Any]:
        payload = {
            "model": self.ollama_model,
            "prompt": f"{SYSTEM_PROMPT}\n\nAnaliza esta página de manga:",
            "images": [image_base64],
            "stream": False,
            "options": {"temperature": 0.1},
        }
        try:
            data = json.dumps(payload).encode()
            req = urllib.request.Request(
                self.ollama_url, data=data,
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=300) as resp:
                result = json.loads(resp.read())
                response_text = result.get("response", "{}")
                return json.loads(response_text)
        except Exception as e:
            print(f"  [AVISO] Ollama falló. Usando fallback.")
            print(f"  [AVISO] Error: {e}")
            return {**{"error": str(e)}, **_intelligent_fallback(filename, self.manga_series)}

    def _call_gemini(self, prompt: str, image_bytes: bytes, mime: str) -> str:
        from google import genai
        client = genai.Client(api_key=self.gemini_api_key)
        image_part = genai.types.Part.from_bytes(data=image_bytes, mime_type=mime)
        response = client.models.generate_content(
            model=self.gemini_model,
            contents=[prompt, image_part],
            config={"temperature": 0.1},
        )
        if response.prompt_feedback and response.prompt_feedback.block_reason:
            raise RuntimeError(f"Gemini blocked: {response.prompt_feedback.block_reason}")
        return response.text

    def _extract_json(self, text: str) -> Dict[str, Any]:
        text = text.strip()
        import re
        m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
        if m:
            text = m.group(1)
        text = text.strip()
        return json.loads(text)

    def _analyze_gemini(self, image_base64: str, filename: str) -> Dict[str, Any]:
        import base64 as b64_mod
        import time
        try:
            image_bytes = b64_mod.b64decode(image_base64)
        except Exception as e:
            return {**{"error": f"base64_decode: {e}"}, **_intelligent_fallback(filename)}
        mime = "image/png"
        if image_bytes[:4] == b"\xff\xd8\xff\xe0" or image_bytes[:4] == b"\xff\xd8\xff\xe1":
            mime = "image/jpeg"
        elif image_bytes[:4] == b"\x89PNG":
            mime = "image/png"
        elif image_bytes[:4] == b"GIF8":
            mime = "image/gif"
        elif image_bytes[:2] == b"BM":
            mime = "image/bmp"
        prompt = SYSTEM_PROMPT + "\n\nAnaliza esta página de manga:"
        last_err = None
        for attempt in range(2):
            try:
                text = self._call_gemini(prompt, image_bytes, mime)
                result = self._extract_json(text)
                if result.get("characters") and len(result["characters"]) > 0:
                    return result
                last_err = "empty characters in response"
            except Exception as e:
                last_err = str(e)
            if attempt == 0:
                time.sleep(2)
        print(f"  [AVISO] Gemini falló. Usando fallback basado en nombre de archivo.")
        if "quota" in str(last_err).lower() or "resource_exhausted" in str(last_err).lower():
            print(f"  [AVISO] Cuota de API agotada. Espera 24h o usa una API key de pago.")
        print(f"  [AVISO] Error: {last_err}")
        return {**{"error": str(last_err)}, **_intelligent_fallback(filename, self.manga_series)}

    def analyze(self, image_base64: str, filename: str = "", manga_series: str = "") -> Dict[str, Any]:
        self.manga_series = manga_series
        if self.backend == "gemini":
            return self._analyze_gemini(image_base64, filename)
        return self._analyze_ollama(image_base64, filename)
