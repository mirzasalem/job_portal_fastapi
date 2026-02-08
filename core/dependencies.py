from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import decode_token
from app.crud.user import get_user_by_email
from app.models.user import User, UserRole

# HTTP Bearer token scheme
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """Get the current authenticated user from JWT token."""
    token = credentials.credentials
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = decode_token(token)
    if payload is None:
        raise credentials_exception
    
    email: str = payload.get("sub")
    token_type: str = payload.get("type")
    
    if email is None or token_type != "access":
        raise credentials_exception
    
    user = get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    
    return user


async def get_current_employer(
    current_user: User = Depends(get_current_user)
) -> User:
    """Verify that the current user is an employer."""
    if current_user.role != UserRole.EMPLOYER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only employers can access this resource"
        )
    return current_user


async def get_current_job_seeker(
    current_user: User = Depends(get_current_user)
) -> User:
    """Verify that the current user is a job seeker."""
    if current_user.role != UserRole.JOB_SEEKER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only job seekers can access this resource"
        )
    return current_user
