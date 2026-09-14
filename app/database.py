from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

SessionLocal=sessionmaker(bind=engine)

def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()


from app.models.user import User
from app.models.movie import Movie
from app.models.watchlist import Watchlist
from app.models.movie_prerequisite import MoviePrerequisite

Base.metadata.create_all(bind=engine)