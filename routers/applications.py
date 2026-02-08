from fastapi import APIRouter, Depends, HTTPException, FastAPI

from sqlalchemy.orm import Session
from app.core.database import get_db
from app import models, schemas
# from app.core.auth import get_current_user
app = FastAPI()
router = APIRouter()


@router.get("/applications/", tags=["applications"])
async def read_applications():
    return [{"application_id": 1, "status": "pending"}, {"application_id": 2, "status": "approved"}]

@router.post("/applications/", tags=["applications"])
async def create_application():
    return {"message": "Application created successfully"}

@router.put("/applications/", tags=["applications"])
async def update_application():
    return {"message": "Application updated successfully"}

@router.delete("/applications/", tags=["applications"])
async def delete_application():
    return {"message": "Application deleted successfully"}

app.include_router(router)


