from sqlalchemy import Column, String, Text, Integer, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.session import Base

class Scene(Base):
    __tablename__ = "scenes"

    manga_page_reference = Column(String)  # Reference to source manga page
    description = Column(Text)
    dialogue = Column(JSON)  # List of dialogue objects
    actions = Column(JSON)
    duration = Column(Float)  # Target duration in seconds
    shot_type = Column(String(50))  # wide, medium, close-up, etc.
    camera_movement = Column(String(50))  # static, pan, tilt, dolly, etc.

    # Foreign keys
    environment_id = Column(Integer, ForeignKey("environments.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))

    # Relationships
    environment = relationship("Environment", back_populates="scenes")
    job = relationship("Job", back_populates="scenes")
    characters = relationship("SceneCharacter", back_populates="scene")

class SceneCharacter(Base):
    __tablename__ = "scene_characters"

    scene_id = Column(Integer, ForeignKey("scenes.id"), primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id"), primary_key=True)

    # Relationships
    scene = relationship("Scene", back_populates="characters")
    character = relationship("Character", back_populates="scenes")