from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.security import get_current_user,get_current_admin
from app.models.user import User

from app.database import get_db
from app.models.movie import Movie
from app.schemas.movie import MovieCreate,MovieUpdate

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/")
def get_movies(search : str | None = None, 
               skip : int = 0,
               limit : int = 10,
               current_user : User = Depends(get_current_user),
               db : Session = Depends(get_db)):

    statement = select(Movie)

    if search:
        statement = statement.where(Movie.title.ilike(f"%{search}%"))

    statement=statement.offset(skip).limit(limit)

    result=db.execute(statement)
    movies=result.scalars().all()

    return movies

@router.get("/{movie_id}")
def get_movie(movie_id : int,
               current_user : User = Depends(get_current_user),
               db : Session = Depends(get_db)):

    statement=select(Movie).where(Movie.id == movie_id)
    result=db.execute(statement)
    movie=result.scalar_one_or_none()

    if movie is None : 
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    return movie

@router.post("/")
def create_movie(movie : MovieCreate,
                 current_user: User = Depends(get_current_admin),
                 db : Session = Depends(get_db)):

    new_movie= Movie(
        title = movie.title,
        release_date = movie.release_date,
        description = movie.description
    )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie

@router.put("/{movie_id}")
def update_movie(movie_id : int,
                movie_data : MovieUpdate,
                 current_user : User = Depends(get_current_admin),
                db : Session = Depends(get_db)
                 ):

    statement = select(Movie).where(Movie.id == movie_id)
    result=db.execute(statement)
    movie=result.scalar_one_or_none()

    if movie is None :
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    movie.title = movie_data.title
    movie.release_date = movie_data.release_date
    movie.description = movie_data.description

    db.commit()
    db.refresh(movie)

    return movie

@router.delete("/{movie_id}")
def delete_movie(movie_id : int , 
                  current_user : User = Depends(get_current_admin),
                 db : Session = Depends(get_db)):

    statement = select(Movie).where(Movie.id == movie_id)
    result = db.execute(statement)
    movie = result.scalar_one_or_none()

    if movie is None : 
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    db.delete(movie)
    db.commit()

    return {
        "message" : "Movie deleted successfully"
    }
    

