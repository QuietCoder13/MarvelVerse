from pydantic import BaseModel
from datetime import date

class MovieCreate(BaseModel):
    title : str
    release_date : date
    description : str

class MovieUpdate(BaseModel):
    title : str
    release_date : date
    description : str