from fastapi import APIRouter, Depends, HTTPException, FastAPI

from sqlalchemy.orm import Session
from app.core.database import get_db
from app import models, schemas
from app.schemas import applications, auth
from app.models.auth import Authentication
from app.core.dependencies import get_db
# from app.core.auth import get_current_user
app = FastAPI()
router = APIRouter()


@router.get("/authentication/", tags=["Authentication"])
async def read_applications(db: Session = Depends(get_db)):
    authentication = db.query(Authentication).all()
    return authentication

@router.post("/authentication/", tags=["Authentication"])
def create_application(item: auth.AuthenticationCreate, db: Session = Depends(get_db)):
    authentication = Authentication(
        name=item.name,
        description=item.description
    )
    db.add(authentication)
    db.commit()
    db.refresh(authentication)


    return {"id": authentication.id, "name": item.name, "description": item.description}

@router.put("/authentication/{authentication_id}", tags=["Authentication"])
def update_application(
    authentication_id: int,
    item: auth.AuthenticationCreate,
    db: Session = Depends(get_db)
):
    authentication = db.query(Authentication).filter(Authentication.id == authentication_id).first()
    if not authentication:
        raise HTTPException(status_code=404, detail="Authentication not found")

    if item.name is not None:
        authentication.name = item.name
    if item.description is not None:
        authentication.description = item.description

    db.commit()
    db.refresh(authentication)

    return {
        "message": "Authentication updated successfully",
        "authentication": authentication
    }

@router.delete("/authentication/{authentication_id}", tags=["Authentication"])
async def delete_authentication(authentication_id: int, db: Session = Depends(get_db)):
    authentication = db.query(Authentication).filter(Authentication.id == authentication_id).first()
    if not authentication:
        raise HTTPException(status_code=404, detail="Authentication not found")
    db.delete(authentication)
    db.commit()
    return {"message": "Authentication deleted successfully"}

# app.include_router(router)


