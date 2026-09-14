from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.movie import Movie
from app.models.movie_prerequisite import MoviePrerequisite

router = APIRouter(
    prefix="/movies",
    tags=["Prerequisites"]
)

@router.get("/{movie_id}/prerequisites")
def get_prerequisites(
    movie_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    movie_statement = select(Movie).where(Movie.id == movie_id)

    movie_result = db.execute(movie_statement)
    movie = movie_result.scalar_one_or_none()

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    statement = (
        select(Movie)
        .join(
            MoviePrerequisite,
            MoviePrerequisite.prerequisite_movie_id == Movie.id
        )
        .where(MoviePrerequisite.movie_id == movie_id)
        .order_by(Movie.release_date)
    )

    result = db.execute(statement)
    prerequisites = result.scalars().all()

    if not prerequisites:
        raise HTTPException(
            status_code=404,
            detail="No prerequisites found for this movie"
        )

    return {
    "movie": movie.title,
    "recommended_before": [
        {
            "id": prerequisite.id,
            "title": prerequisite.title,
            "release_date": prerequisite.release_date
        }
        for prerequisite in prerequisites
    ]
}