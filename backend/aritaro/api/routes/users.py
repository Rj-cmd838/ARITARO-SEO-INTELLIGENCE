from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from aritaro.domains.project import Project
from aritaro.domains.website import Website
from fastapi.security import OAuth2PasswordBearer
from aritaro.core.security import verify_access_token
from aritaro.core.dependencies import get_current_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

from aritaro.core.database import get_db
from aritaro.core.security import (
    hash_password,
    verify_password,
    create_access_token)
from aritaro.domains.user import User
from aritaro.schemas.user import (
    UserCreate, 
    UserResponse,
    LoginRequest,
    TokenResponse)
     
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.post(
    "/login",
    response_model=TokenResponse
)
def login_user(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == login_data.email
    ).first()

    if not user or not verify_password(
        login_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"sub": str(user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me", response_model=UserResponse)
def get_my_profile(
    current_user: User = Depends(get_current_user)
):
    return current_user
