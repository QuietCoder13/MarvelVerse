from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import jwt
import os

from app.database import get_db
from app.models.user import User

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")

password_hash=PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password : str, hashed_password:str) -> bool :
        return password_hash.verify(password,hashed_password)


def create_access_token(data:dict) -> str :
      expire = datetime.now(timezone.utc) + timedelta(minutes=30)

      data = data.copy()
      data.update({"exp": expire})

      token= jwt.encode(data,SECRET_KEY,algorithm="HS256")
      return token

def decode_access_token(token:str):
        try:
            payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )
            return payload

        except jwt.InvalidTokenError:
                raise HTTPException(
                status_code=401,
                detail="Invalid or expired token"
        )

def get_current_user(
            token:str = Depends(oauth2_scheme),
            db : Session =Depends(get_db)
):

      payload=decode_access_token(token)
      user_id=payload.get("user_id")

      if user_id is None:
            raise HTTPException(
                  status_code=401,
                  detail="Invalid access token"
            )

      statement=select(User).where(User.id == user_id)
      result=db.execute(statement)
      user=result.scalar_one_or_none()

      if user is None:
            raise HTTPException(
                  status_code=404,
                  detail="User not found"
            )
      return user

def get_current_admin(
            current_user : User = Depends(get_current_user)
):
       if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

        return current_user
