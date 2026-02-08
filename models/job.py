from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    
    applications = relationship("Application", back_populates="job")

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(100), nullable=False)
    description = Column(Text, default="Unspecified")

    company_name = Column(String(200), nullable=False)
    location = Column(String(100), default="Unspecified")

    employment_type = Column(String(50), nullable=True)  # full-time / part-time / remote
    experience_level = Column(String(50), nullable=True)

    salary_min = Column(Float, nullable=True)
    salary_max = Column(Float, nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
