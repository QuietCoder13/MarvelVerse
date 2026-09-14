from app.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from datetime import date



class Movie(Base):
    __tablename__="movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column()
    release_date : Mapped[date]=mapped_column()
    description : Mapped[str] = mapped_column()