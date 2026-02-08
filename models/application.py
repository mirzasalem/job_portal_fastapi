from sqlalchemy import Column, Integer, Boolean, String, Text, DateTime, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    # user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)

    applied_at = Column(DateTime(timezone=True), server_default=func.now())

    status = Column(Boolean, default=True)

    resume_url = Column(String(220), default="Unspecified")
    cover_letter = Column(Text, default="Unspecified")

    # Relationships
    # user = relationship("User", back_populates="applications")
    job = relationship("Job", back_populates="applications")