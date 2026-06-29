import enum
from sqlalchemy import Column, Integer, String, Text, JSON, ForeignKey
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import relationship
from app.db.session import Base

class AssetType(str, enum.Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    EFFECT = "effect"
    MUSIC = "music"

class Asset(Base):
    __tablename__ = "assets"

    asset_type = Column(SAEnum(AssetType), nullable=False)
    file_path = Column(String(500), nullable=False)  # Path or URL to file
    file_size = Column(Integer)  # Size in bytes
    mime_type = Column(String(100))
    generation_metadata = Column(JSON)  # Generation parameters, prompts, etc.

    # Relationships (optional, for tracking what this asset is used for)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
    scene_id = Column(Integer, ForeignKey("scenes.id"), nullable=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=True)

    job = relationship("Job", back_populates="assets")