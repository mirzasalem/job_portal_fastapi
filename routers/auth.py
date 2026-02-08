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


from fastapi import APIRouter, Depends, HTTPException, FastAPI

from sqlalchemy.orm import Session
from app.core.database import get_db
from app import models, schemas
# from app.core.auth import get_current_user
app = FastAPI()
router = APIRouter()


@router.get("/auth/", tags=["auth"])
async def read_auth():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.post("/auth/", tags=["auth"])
async def create_auth():
    return {"message": "Auth created successfully"}

@router.put("/auth/", tags=["auth"])
async def update_auth():
    return {"message": "Auth updated successfully"}

@router.delete("/auth/", tags=["auth"])
async def delete_auth():
    return {"message": "Auth deleted successfully"}

# app.include_router(router)


