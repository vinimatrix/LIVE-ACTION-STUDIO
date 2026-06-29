from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import declared_attr

class BaseModel:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())