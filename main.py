from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.routers import jobs, applications, auth
from app.models import job

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()



app.include_router(auth.router)
app.include_router(jobs.router)
app.include_router(applications.router)


@app.get("/" ,tags= ["Start"])
def root():
    """Root endpoint - API health check."""
    return {
        "message": "Welcome to Job Portal API",
        "version": "1",
        "Owner": "Mirza Salem",
        "status": "active"
    }

