import enum
from sqlalchemy import Column, String, Text, Integer, Float, ForeignKey
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import relationship
from app.db.session import Base

class JobStatus(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class Job(Base):
    __tablename__ = "jobs"

    manga_filename = Column(String(255), nullable=False)
    status = Column(SAEnum(JobStatus), default=JobStatus.PENDING)
    progress = Column(Integer, default=0)  # Percentage 0-100
    current_step = Column(String(100))  # Current processing step
    error_message = Column(Text, nullable=True)
    total_duration = Column(Float)  # Total video duration in seconds

    # Relationships
    assets = relationship("Asset", back_populates="job")
    scenes = relationship("Scene", back_populates="job")