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
        title=item.title,
        company_name=item.company_name,
        location=item.location,
        employment_type=item.employment_type,
        experience_level=item.experience_level,
        salary_min=item.salary_min,
        salary_max=item.salary_max,
        # description=item.description
    )
    db.add(job)
    db.commit()
    db.refresh(job)


    return {"id": job.id, "title": item.title, "company_name": item.company_name, "location": item.location}
    # return {"id": job.id, "title": item.title, "company_name": item.company_name, "location": item.location}


@router.put("/jobs/{job_id}", tags=["Jobs"])
def update_job(
    job_id: int,
    item: jobs.JobCreate,
    db: Session = Depends(get_db)
):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    for field, value in item.dict(exclude_unset=True).items():
        setattr(job, field, value)      

    db.commit()
    db.refresh(job)
        
    return {"message": "Job updated successfully", "id": job.id, "title": item.title, "company_name": item.company_name, "location": item.location}

@router.delete("/jobs/{job_id}", tags=["Jobs"])
async def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(job)
    db.commit()
    return {"message": "Job deleted successfully"}

# app.include_router(router)


