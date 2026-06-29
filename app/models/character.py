from sqlalchemy import Column, String, Text, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Character(Base):
    __tablename__ = "characters"

    name = Column(String(100), nullable=False, index=True)
    description = Column(Text)
    visual_references = Column(JSON)  # URLs to reference images
    personality_traits = Column(JSON)
    expressions = Column(JSON)  # Available facial expressions
    outfits = Column(JSON)  # List of outfit objects with references
    weapons = Column(JSON)  # List of weapon objects
    abilities = Column(JSON)  # List of special abilities/powers
    voice_profile = Column(String)  # Reference to voice model

    # Relationships
    scenes = relationship("SceneCharacter", back_populates="character")