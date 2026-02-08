from fastapi import APIRouter, Depends, HTTPException, FastAPI

from sqlalchemy.orm import Session
from app.core.database import get_db
from app import models, schemas
from app.schemas import applications
from app.models.application import Application
from app.core.dependencies import get_db
# from app.core.auth import get_current_user
app = FastAPI()
router = APIRouter()


@router.get("/applications/", tags=["Applications"])
async def read_applications(db: Session = Depends(get_db)):
    applications = db.query(Application).all()
    return applications

@router.post("/application/", tags=["Applications"])
def create_application(item: applications.ApplicationCreate, db: Session = Depends(get_db)):
    application = Application(
        job_id=item.job_id,
        resume_url=item.resume_url,
        cover_letter=item.cover_letter
    )
    db.add(application)
    db.commit()
    db.refresh(application)


    return {"message": "Application created successfully", "Created Application": application}

@router.put("/applications/{application_id}", tags=["Applications"])
def update_application(
    application_id: int,
    item: applications.ApplicationCreate,
    db: Session = Depends(get_db)
):
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    for field, value in item.dict(exclude_unset=True).items():
        setattr(application, field, value)  

    db.commit()
    db.refresh(application)

    return {
        "message": "Application updated successfully",
        "application": application
    }

@router.delete("/applications/{application_id}", tags=["Applications"])
async def delete_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(application)
    db.commit()
    return {"message": "Application deleted successfully"}

# app.include_router(router)


