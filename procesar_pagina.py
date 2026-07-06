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
        
        all_prompts = []
        for asset in assets:
            prompt_text = asset.generation_metadata.get("prompt", "")
            all_prompts.append(prompt_text)
            all_prompts.append("\n" + "=" * 80 + "\n")
            
        # Escribir en archivo de salida
        output_dir = os.path.dirname(args.output)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            
        with open(args.output, "w", encoding="utf-8") as out_file:
            out_file.write("\n".join(all_prompts))
            
        print(f"\n=== PROMPTS ESTRUCTURADOS GENERADOS ({len(assets)} ESCENAS) ===")
        for prompt in all_prompts:
            print(prompt)
            
        print(f"\nPrompts estructurados guardados en: {args.output}")
        
    finally:
        db.close()

if __name__ == "__main__":
    main()
