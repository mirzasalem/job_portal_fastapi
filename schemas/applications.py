from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ApplicationCreate(BaseModel):
    # user_id: int
    job_id: int
    resume_url: Optional[str] = "Unspecified"
    cover_letter: Optional[str] = "Unspecified"

class ApplicationResponse(BaseModel):
    id: int
    # user_id: int
    job_id: int
    applied_at: datetime
    status: bool
    resume_url: str
    cover_letter: str

    class Config:
        from_attributes = True  # Allows SQLAlchemy model → Pydantic
