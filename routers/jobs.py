from fastapi import APIRouter, Depends, HTTPException, FastAPI

from sqlalchemy.orm import Session
from app.core.database import get_db
from app import models, schemas
# from app.core.auth import get_current_user
app = FastAPI()
router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.post("/users/", tags=["users"])
async def create_user():
    return {"message": "User created successfully"}

@router.put("/users/", tags=["users"])
async def update_user():
    return {"message": "User updated successfully"}

@router.delete("/users/", tags=["users"])
async def delete_user():
    return {"message": "User deleted successfully"}


# app.include_router(router)


