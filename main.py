from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.routers import jobs, applications, auth

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()



app.include_router(auth.router)
app.include_router(jobs.router)
app.include_router(applications.router)


@app.get("/")
def root():
    """Root endpoint - API health check."""
    return {
        "message": "Welcome to Job Portal API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "active"
    }

