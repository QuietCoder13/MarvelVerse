from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models.movie import Movie
from app.schemas.movie import MovieCreate,MovieUpdate
from app.routes import movies,auth

app=FastAPI()

app.include_router(movies.router)
app.include_router(auth.router)