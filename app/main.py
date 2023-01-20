from fastapi import FastAPI, status
from app.schema import Movies
from .database import connection, cursor


app = FastAPI()


@app.get("/movies")
async def list_movies():
    cursor.execute("SELECT * FROM movies")

    return {"data": cursor.fetchall()}


@app.post("/movies", status_code=status.HTTP_201_CREATED)
async def create_movies(data: Movies):
    return data


