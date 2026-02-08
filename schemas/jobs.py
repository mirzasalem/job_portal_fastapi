from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app import models, schemas
from app.core.auth import get_current_user          
router = APIRouter()
