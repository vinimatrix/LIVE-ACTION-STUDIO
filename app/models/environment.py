from sqlalchemy import Column, String, Text, JSON
from sqlalchemy.orm import relationship
from app.db.session import Base

class Environment(Base):
    __tablename__ = "environments"

    name = Column(String(100), nullable=False, index=True)
    description = Column(Text)
    location_type = Column(String(50))  # city, interior, forest, castle, etc.
    visual_references = Column(JSON)
    lighting_conditions = Column(JSON)  # Time of day, weather, etc.
    props = Column(JSON)  # Objects present in the environment

    # Relationships
    scenes = relationship("Scene", back_populates="environment")