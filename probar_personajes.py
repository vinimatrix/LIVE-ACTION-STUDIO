from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import Base
from app.agents.character_manager.character_manager import CharacterManagerAgent

# 1. Configurar una base de datos local para la prueba
engine = create_engine("sqlite:///./prueba_local.db")
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. Inicializar el agente de personajes
agente = CharacterManagerAgent(db_session=SessionLocal)

# 3. Crear y probar un nuevo personaje
personaje = agente.get_or_create_character("Goku", ["Valiente", "Fuerte", "Hambriento"])
print("Personaje creado/obtenido:", personaje)

# 4. Procesar un guión (Screenplay) simulando que el agente recibe datos de escena
screenplay_data = {
    "scene_id": 1,
    "dialogue": [
        {"character": "Goku", "text": "¡Kamehameha!", "emotion": "determinado"}
    ],
    "actions": ["Goku lanza su técnica especial."]
}

resultado = agente.process_screenplay(screenplay_data)
print("\nResultado del guión procesado:", resultado)
