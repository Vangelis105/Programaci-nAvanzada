from sqlmodel import SQLModel, Field

class MoviesModel(SQLModel, table=True):
    
    __tablename__ = "MOVIES"
    
    id: int = Field(primary_key=True)
    title: str
    duration: int
    release_year: int
    director: str
    rating: str
    genre: str
    