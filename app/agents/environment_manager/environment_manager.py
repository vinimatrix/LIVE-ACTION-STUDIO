from typing import Dict, Any, Callable
from app.core.config import settings
from app.models import Environment
from app.db.session import SessionLocal


class EnvironmentManagerAgent:
    def __init__(self, db_session: Callable = None):
        self.settings = settings
        self._db_session = db_session or SessionLocal

    def get_or_create_environment(
        self, location_type: str, name: str = None
    ) -> Dict[str, Any]:
        db = self._db_session()
        try:
            environment = None
            if name:
                environment = db.query(Environment).filter(
                    Environment.name == name
                ).first()

            if not environment:
                environment = db.query(Environment).filter(
                    Environment.location_type == location_type
                ).first()

            if environment:
                db.commit()
                db.refresh(environment)
            else:
                environment = Environment(
                    name=name or f"{location_type}_{db.query(Environment).count() + 1}",
                    description=f"A {location_type} environment",
                    location_type=location_type,
                    visual_references=[],
                    lighting_conditions={"time_of_day": "day", "weather": "clear"},
                    props=[]
                )
                db.add(environment)
                db.commit()
                db.refresh(environment)

            return {
                "id": environment.id,
                "name": environment.name,
                "location_type": environment.location_type,
                "visual_references": environment.visual_references,
                "lighting_conditions": environment.lighting_conditions,
                "props": environment.props
            }
        finally:
            db.close()

    def process_screenplay(self, screenplay_data: Dict[str, Any]) -> Dict[str, Any]:
        environment_data = self.get_or_create_environment(
            "interior", "Default Interior"
        )

        enhanced = screenplay_data.copy()
        enhanced["environment_data"] = environment_data

        return enhanced
