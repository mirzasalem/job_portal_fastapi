from fastapi import FastAPI
from pydantic import BaseModel




class AuthenticationCreate(BaseModel):
    name: str
    description: str | None = None
