from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from models import MoviesModel
from sqlmodel import select
from schemas import MovieSchema

app = FastAPI()


create_db_and_tables()

@app.post("/movies")
async def create_movie(database: SessionDep, movie_data: MovieSchema):
    movie = MoviesModel(title=movie_data.title, duration=movie_data.duration, release_year=movie_data.release_year, director=movie_data.director, rating=movie_data.rating, genre=movie_data.genre)
    database.add(movie)
    database.commit()
    database.refresh(movie)
    return movie

@app.get("/movies")
async def get_movies(database: SessionDep):
    statement = select(MoviesModel)
    results = database.exec(statement=statement)
    items = results.all()
    return items

@app.get("/movies/{movie_id}")
async def get_movie_by_id(movie_id: int, database: SessionDep):
    movie = database.get(MoviesModel, movie_id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Film nicht gefunden")
    return movie