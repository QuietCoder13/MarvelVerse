from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserCreate
from app.database import get_db
from app.models.user import User
from app.core.security import hash_password,verify_password,create_access_token


router = APIRouter(prefix="/auth" , tags=["Authentication"])

@router.post("/register")
def register_user(user_data:UserCreate,
                  db: Session = Depends(get_db)):

    statement=select(User).where(User.email == user_data.email)
    result = db.execute(statement)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"

        )

    new_user=User (
        email = user_data.email,
        password_hash = hash_password(user_data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message" : "User registered successfully",
        "user_id" : new_user.id
    }

@router.post("/login")
def login_user(user_data : OAuth2PasswordRequestForm = Depends(),
                db : Session = Depends(get_db)):

    statement= select(User).where(User.email == user_data.username)
    result = db.execute(statement)
    user = result.scalar_one_or_none()

    if user is None :
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not verify_password(user_data.password,user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token=create_access_token({
        "user_id":user.id
    })

    return {
    "access_token" : access_token,
    "token_type" : "bearer"

    }


