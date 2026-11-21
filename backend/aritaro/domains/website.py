
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from aritaro.core.database import Base


class Website(Base):
    __tablename__ = "websites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    url = Column(String(500), unique=True, nullable=False)

    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    project = relationship("Project", back_populates="websites")
