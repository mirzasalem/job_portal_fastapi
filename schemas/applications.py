from fastapi import FastAPI
from pydantic import BaseModel




class ApplicationCreate(BaseModel):
    name: str
    description: str | None = None
