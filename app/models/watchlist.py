from sqlalchemy import ForeignKey,Boolean,UniqueConstraint
from sqlalchemy.orm import mapped_column,Mapped
from app.database import Base

class Watchlist(Base):
    __tablename__ = "watchlist"

    __table_args__= ( UniqueConstraint("user_id","movie_id", name="uq_user_movie"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"), nullable=False)
    movie_id = mapped_column(ForeignKey("movies.id"), nullable=False)
    watched = mapped_column(Boolean, default=False, nullable=False)