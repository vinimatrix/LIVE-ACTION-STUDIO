import os
import sys
import json
import base64
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Agregar el directorio actual al path para importar la app
sys.path.append(os.getcwd())

from app.db.session import Base
from app.models import Job, Scene, Asset
from app.agents.director.director import DirectorAgent
from app.agents.storyboard.storyboard import StoryboardAgent
from app.agents.flow_prompt_builder.flow_prompt_builder import FlowPromptBuilderAgent

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Procesa una página de manga para generar prompts estructurados fotorrealistas con anti-alucinación."
    )
    parser.add_argument(
        "--image", 
        type=str, 
        required=True, 
        help="Ruta al archivo de imagen de la página de manga (JPG, PNG)."
    )
    parser.add_argument(
        "--manga",
        type=str,
        default="",
        help="Nombre del manga (ej: boruto, naruto) para mejorar el análisis cuando la API de visión falla."
    )
    parser.add_argument(
        "--char_map", 
        type=str, 
        default="{}", 
        help="JSON string con el mapeo de nombres de personajes del manga a referencias en Flow, ej: '{\"Sarada\": \"Sarada_Flow_Ref\"}'"
    )
    parser.add_argument(
        "--max_scenes", 
        type=int, 
        default=5, 
        help="Número máximo de escenas a segmentar (por defecto 5)."
    )
    parser.add_argument(
        "--output", 
        type=str, 
        default="final_output/prompts_generados.txt", 
        help="Archivo donde se guardarán los prompts estructurados generados."
    )
    return parser.parse_args()

def encode_image_to_base64(image_path: str) -> str:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No se encontró el archivo de imagen en: {image_path}")
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def main():
    # Evitar errores de codificación en consolas Windows
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        
    args = parse_arguments()
    
    print("=== CONFIGURANDO BASE DE DATOS LOCAL (SQLite) ===")
    DB_URL = "sqlite:///./manga_prompts.db"
    engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    Base.metadata.create_all(bind=engine)
    
    # Intentar leer mapeo de personajes
    try:
        character_mapping = json.loads(args.char_map)
    except Exception as e:
        print(f"Error parseando --char_map (debe ser un JSON válido): {e}")
        sys.exit(1)
        
    print(f"\n=== LEYENDO Y CODIFICANDO IMAGEN: {args.image} ===")
    try:
        image_base64 = encode_image_to_base64(args.image)
    except Exception as e:
        print(f"Error codificando imagen: {e}")
        sys.exit(1)
        
    filename = os.path.basename(args.image)
    
    # Construir petición
    manga_request = {
        "filename": filename,
        "manga": args.manga,
        "image": image_base64,
        "character_mapping": character_mapping,
        "options": {
            "max_scenes": args.max_scenes
        }
    }
    
    print("\n=== INICIALIZANDO PIPELINE DE ANÁLISIS ===")
    director = DirectorAgent(db_session=SessionLocal)
    
    print("\n=== PROCESANDO PÁGINA DE MANGA CON AGENTES (MangaAnalyzer + SceneComposer + FlowPromptBuilder) ===")
    print("Nota: Si Ollama no está corriendo localmente en el puerto 11434, se usará lógica de fallback simulada.")
    
    job_id = director.process_manga_request(manga_request)
    
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        print(f"\n¡PROCESAMIENTO COMPLETADO EXITOSAMENTE!")
        print(f"Job ID: {job.id}")
        
        # Recuperar los prompts generados de los assets
        assets = db.query(Asset).filter(Asset.job_id == job_id, Asset.asset_type == "prompt").all()
        
        if not assets:
            print("No se generaron prompts. Revisa los logs de Ollama o del agente.")
            return
            
        # Ordenar por número de escena
        assets = sorted(assets, key=lambda a: a.generation_metadata.get("scene_number", 0))
        
        all_scene_prompts = []
        for asset in assets:
            prompt_text = asset.generation_metadata.get("prompt", "")
            all_scene_prompts.append(prompt_text)
            all_scene_prompts.append("\n" + "=" * 80 + "\n")

        # ── 2. GENERAR STORYBOARD PROMPTS ──
        print("\n=== GENERANDO PROMPTS DE STORYBOARD ===")
        scenes_data = []
        scenes_db = db.query(Scene).filter(Scene.job_id == job_id).all()
        for sc in scenes_db:
            sc_meta = next((a.generation_metadata for a in assets if a.scene_id == sc.id), {})
            scenes_data.append({
                "scene_id": sc.id,
                "duration": sc.duration,
                "characters": sc_meta.get("characters", []),
                "description": sc.description,
                "camera": sc_meta.get("camera", {}),
                "lighting": sc_meta.get("lighting", {}),
                "dialogue": sc_meta.get("dialogue", []),
                "transition": "cut"
            })

        storyboard_agent = StoryboardAgent()
        prompt_builder = FlowPromptBuilderAgent()
        storyboard_prompts = prompt_builder.build_storyboard_prompts(
            scenes_data, character_mapping, storyboard_agent
        )

        all_storyboard_prompts = []
        for sp in storyboard_prompts:
            all_storyboard_prompts.append(sp["prompt_text"])
            all_storyboard_prompts.append("\n" + "=" * 80 + "\n")

        # ── 3. GUARDAR ARCHIVO DE SALIDA ──
        output_dir = os.path.dirname(args.output)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        output_lines = []
        output_lines.append("=== PROMPTS DE ESCENA ===")
        output_lines.append("")
        output_lines.extend(all_scene_prompts)
        output_lines.append("")
        output_lines.append("=" * 80)
        output_lines.append("")
        output_lines.append("=== PROMPTS DE STORYBOARD ===")
        output_lines.append("")
        output_lines.extend(all_storyboard_prompts)

        with open(args.output, "w", encoding="utf-8") as out_file:
            out_file.write("\n".join(output_lines))

        print(f"\n=== RESULTADOS ===")
        print(f"Prompts de escena generados: {len(assets)}")
        print(f"Prompts de storyboard generados: {len(storyboard_prompts)}")
        print(f"\nArchivo guardado en: {args.output}")
        print(f"\n--- PRIMER PROMPT DE STORYBOARD ---")
        if all_storyboard_prompts:
            print(all_storyboard_prompts[0])
        
    finally:
        db.close()

if __name__ == "__main__":
    main()
