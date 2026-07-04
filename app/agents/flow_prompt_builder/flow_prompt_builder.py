from typing import Dict, Any, List


class FlowPromptBuilderAgent:
    def build_prompts(self, scenes: List[Dict[str, Any]], character_mapping: Dict[str, str]) -> List[Dict[str, Any]]:
        prompts = []
        for i, scene in enumerate(scenes):
            prompt_text = self._build_prompt(scene, character_mapping, i + 1)
            prompts.append({
                "scene_id": scene["scene_id"],
                "scene_number": i + 1,
                "duration": scene["duration"],
                "prompt_text": prompt_text
            })
        return prompts

    def _build_prompt(self, scene: Dict[str, Any], character_mapping: Dict[str, str], scene_num: int) -> str:
        duration = scene.get("duration", 8.0)
        start_time = sum(scene.get("duration", 8.0) for _ in range(scene_num - 1))
        end_time = start_time + duration

        lines = []
        lines.append(f"ESCENA {scene_num} ({self._fmt_time(start_time)} - {self._fmt_time(end_time)})")
        lines.append("─" * 50)
        lines.append("")

        # PERSONAJES
        lines.append("PERSONAJES:")
        for c in scene.get("characters", []):
            name = c.get("name", "Unknown")
            flow_ref = character_mapping.get(name, name)
            appearance = c.get("appearance", "")
            expression = c.get("expression", "neutral")
            position = c.get("position", "frame")
            lines.append(f"  - {name} (Flow ref: {flow_ref}): {expression}, {position}")
            if appearance:
                lines.append(f"    Apariencia: {appearance}")
        lines.append("")

        # ESCENARIO
        lines.append("ESCENARIO:")
        lighting = scene.get("lighting", {})
        time_of_day = lighting.get("time_of_day", "day")
        lines.append(f"  - Descripci\u00f3n: {scene.get('description', '')}")
        lines.append(f"  - Hora: {time_of_day}")
        lines.append("")

        # CAMARA
        camera = scene.get("camera", {})
        lines.append("C\u00c1MARA:")
        lines.append(f"  - Shot: {camera.get('shot_type', 'wide')}")
        lines.append(f"  - Movimiento: {camera.get('movement', 'static')}")
        lines.append(f"  - Lente: {camera.get('lens', '35mm f/2.8')}")
        lines.append("")

        # ILUMINACION
        mood = lighting.get("mood_lighting", "neutral")
        lines.append("ILUMINACI\u00d3N:")
        lines.append(f"  - Ambiente: {time_of_day} lighting")
        lines.append(f"  - Mood: {mood}")
        lines.append("")

        # MOOD
        lines.append("MOOD: " + mood.capitalize())
        lines.append("")

        # ACCION
        lines.append("ACCI\u00d3N:")
        lines.append(f"  - {scene.get('description', '')}")
        lines.append(f"  - Duraci\u00f3n: {duration:.1f} segundos")
        for d in scene.get("dialogue", []):
            lines.append(f"  - Di\u00e1logo: [{d.get('character', '?')}] \"{d.get('text', '')}\"")
        lines.append("")

        # SPECS TECNICAS
        lines.append("SPECS T\u00c9CNICAS:")
        lines.append("  - Resoluci\u00f3n: 8K (7680x4320)")
        lines.append("  - Estilo: hiperrealista, cinematogr\u00e1fico")
        lines.append("  - Texturas: detalladas, PBR")
        lines.append("  - Iluminaci\u00f3n: volumetric lighting, global illumination")
        lines.append("  - Post-procesado: color grading cinematogr\u00e1fico, grain sutil")
        lines.append("  - Motion blur: obturador 180\u00b0, natural")
        lines.append("  - Profundidad de campo: acorde al shot")
        lines.append("")

        # ANTI-ALUCINACION
        lines.append("ANTI-ALUCINACI\u00d3N:")
        for name in scene.get("characters", []):
            n = name.get("name", "")
            flow_ref = character_mapping.get(n, n)
            lines.append(f"  - Mantener dise\u00f1o de {n} (ref: {flow_ref}) exactamente como en la referencia de Flow")
        lines.append("  - No a\u00f1adir objetos, personajes o elementos no descritos")
        lines.append("  - Fondo coherente con la descripci\u00f3n del escenario")
        lines.append("  - Respetar iluminaci\u00f3n y hora del d\u00eda especificadas")
        lines.append("  - No cambiar expresiones faciales ni poses indicadas")

        return "\n".join(lines)

    def _fmt_time(self, seconds: float) -> str:
        m = int(seconds // 60)
        s = int(seconds % 60)
        return f"{m:02d}:{s:02d}"
