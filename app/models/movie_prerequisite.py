from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class MoviePrerequisite(Base):
    __tablename__="movie_prerequisites"

    id : Mapped[int] = mapped_column(primary_key=True)

    movie_id : Mapped[int] = mapped_column(
        ForeignKey("movies.id"),
        nullable=False
    )

    prerequisite_movie_id : Mapped[int] = mapped_column(
        ForeignKey("movies.id"),
        nullable=False
    )
