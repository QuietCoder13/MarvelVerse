from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.movie import Movie
from app.models.watchlist import Watchlist

router=APIRouter(prefix="/watchlist", tags=["Watchlist"])

@router.post("/{movie_id}")
def add_to_watchlist(
    movie_id :int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    statement = select(Movie).where(Movie.id == movie_id)
    result = db.execute(statement)
    movie = result.scalar_one_or_none()

    if movie is None:
     raise HTTPException(status_code=404, detail="Movie not found")

    statement = select(Watchlist).where(
        Watchlist.user_id == current_user.id,
        Watchlist.movie_id == movie_id
    )

    result = db.execute(statement)
    existing_item = result.scalar_one_or_none()

    if existing_item:
     raise HTTPException(
        status_code=400,
        detail="Movie already in watchlist"
    )
    new_item = Watchlist(
      user_id=current_user.id,
      movie_id=movie_id
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return {
        "message": "Movie added to watchlist",
        "watchlist_id": new_item.id
    }


@router.get("/")
def get_watchlist(current_user: User = Depends(get_current_user),
                  db : Session = Depends(get_db)
                  ):

  statement = select(Watchlist,Movie).join(Movie,Watchlist.movie_id == Movie.id).where(Watchlist.user_id == current_user.id)
  result = db.execute(statement)
  watchlist_items = result.all()

  return [
        {
            "watchlist_id": watchlist.id,
            "movie_id": movie.id,
            "title": movie.title,
            "release_date": movie.release_date,
            "watched": watchlist.watched
        }
            for watchlist, movie in watchlist_items
        ]

@router.delete("/{movie_id}")
def delete_watchlist(movie_id : int ,
                     current_user : User = Depends(get_current_user),
                     db : Session = Depends(get_db)):
  statement=select(Watchlist).where(Watchlist.movie_id == movie_id, Watchlist.user_id == current_user.id)
  result=db.execute(statement)
  watchlist_item = result.scalar_one_or_none()

  if watchlist_item is None:
    raise HTTPException(
      status_code=404,
      detail="Movie not found in your watchlist"
    )
  db.delete(watchlist_item)
  db.commit()

  return {
    "message" : "Movie removed from watchlist"
  }


@router.patch("/{movie_id}")
def update_watch_status(movie_id : int,
                        watched : bool,
                        current_user : User = Depends(get_current_user),
                        db : Session = Depends(get_db)):

  statement = select(Watchlist).where(Watchlist.movie_id == movie_id, Watchlist.user_id == current_user.id)
  result=db.execute(statement)
  watchlist_item = result.scalar_one_or_none()

  if watchlist_item is None:
    raise HTTPException(
        status_code=404,
        detail="Movie not found in your watchlist"
      )

  watchlist_item.watched = watched

  db.commit()
  db.refresh(watchlist_item)

  return {
        "message": "Watch status updated",
        "movie_id": movie_id,
        "watched": watchlist_item.watched
    }




  
  
