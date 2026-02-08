from fastapi import APIRouter, Depends, HTTPException, FastAPI

from sqlalchemy.orm import Session
from app.core.database import get_db
from app import models, schemas
from app.schemas import jobs
from app.models.job import Job
from app.core.dependencies import get_db
# from app.core.auth import get_current_user
app = FastAPI()
router = APIRouter()


@router.get("/jobs/", tags=["Jobs"])
async def read_jobs(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    return jobs

@router.post("/jobs/", tags=["Jobs"])
def create_job(item: jobs.JobCreate, db: Session = Depends(get_db)):
    job = Job(
        name=item.name,
        description=item.description
    )
    db.add(job)
    db.commit()
    db.refresh(job)


    return {"id": job.id, "name": item.name, "description": item.description}

@router.put("/jobs/{job_id}", tags=["Jobs"])
def update_job(
    job_id: int,
    item: jobs.JobCreate,
    db: Session = Depends(get_db)
):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if item.name is not None:
        job.name = item.name
    if item.description is not None:
        job.description = item.description

    db.commit()
    db.refresh(job)

    return {
        "message": "Job updated successfully",
        "job": job
    }

@router.delete("/jobs/{job_id}", tags=["Jobs"])
async def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(job)
    db.commit()
    return {"message": "Job deleted successfully"}

# app.include_router(router)


