from pydantic import BaseModel
from typing import Optional


class JobCreate(BaseModel):
    title: str
    description: Optional[str] = None
    company_name: str
    location: Optional[str] = "Unspecified"
    employment_type: Optional[str] = None
    experience_level: Optional[str] = None
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
