from fastapi import FastAPI, HTTPException
from models import *
from tortoise.contrib.fastapi import register_tortoise
from pydantic import BaseModel
#Static file config setup
app = FastAPI()

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",  # or your database URL
    modules={"models": ["models"]},
    generate_schemas=True,  # create tables automatically
    add_exception_handlers=True,
)


class JobCreate(BaseModel):
    title: str
    description: str | None = None
    company_name: str
    location: str | None = None
    employment_type: str | None = None
    experience_level: str | None = None
    salary_min: float | None = None
    salary_max: float | None = None
    owner_id: int
    
    
    


@app.get("/users")
async def get_user():
    response = await User_pydantic_all.from_queryset(User.all())
    return {"status": "ok", "data": response}



# CREATE a user
@app.post("/users")
async def create_user(user: User_pydantic):
    user_obj = await User.create(**user.dict(exclude_unset=False))
    user_obj_pydantic = await User_pydantic.from_tortoise_orm(user_obj)
    return {"status": "ok", "data": user_obj_pydantic}



@app.get("/jobs")
async def get_jobs():
    response = await Job_pydantic_all.from_queryset(
        Job.all().select_related("owner")
    )
    return {"status": "ok", "data": response}


# CREATE a user
@app.post("/jobs")
async def create_job(job: JobCreate):
    user = await User.get_or_none(id=job.owner_id)

    if not user:
        return {"status": "Error", "message": HTTPException(status_code=404, detail="User not found")}

    job_obj = await Job.create(
        title=job.title,
        description=job.description,
        company_name=job.company_name,
        location=job.location,
        employment_type=job.employment_type,
        experience_level=job.experience_level,
        salary_min=job.salary_min,
        salary_max=job.salary_max,
        owner=user
    )

    job_pydantic = await Job_pydantic.from_tortoise_orm(job_obj)
    return {"status": "ok", "data": job_pydantic}



# CREATE a Application
@app.post("/applications")
async def create_application(application: Application_pydantic):
    application_obj = await Application.create(**application.dict(exclude_unset=False))
    application_obj_pydantic = await Application_pydantic.from_tortoise_orm(application_obj)
    return {"status": "ok", "data": application_obj_pydantic}
# CREATE a Application
@app.post("/applications")
async def create_job(job: Job_pydantic):
    job_obj = await Job.create(**job.dict(exclude_unset=False))
    job_obj_pydantic = await Job_pydantic.from_tortoise_orm(job_obj)
    return {"status": "ok", "data": job_obj_pydantic}