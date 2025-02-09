from fastapi import FastAPI, HTTPException
from models import Film
from pydantic import BaseModel

app = FastAPI()

# Lista filmova
filmovi = [
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
    {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
    {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
    {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008},
]

class CreateFilm(BaseModel):
    naziv: str
    genre: str
    godina: int

# Definiranje rute GET 
@app.get("/filmovi", response_model=list[Film])
def get_filmovi():
    return filmovi

# Definiranje rute GET id
@app.get("/filmovi/{id}", response_model=Film)
def get_film_by_id(id: int):
    print(f"Tražim film s ID-jem: {id}")
    for film in filmovi:
        print(f"Provjeravam film: {film}")
        if film["id"] == id:
            return film
    raise HTTPException(status_code=404, detail="Film nije pronađen")

# Definiranje rute POST 
@app.post("/filmovi", response_model=Film)
def create_film(film: CreateFilm):
    new_id = max(f["id"] for f in filmovi) + 1 if filmovi else 1
    new_film = {"id": new_id, **film.dict()}
    filmovi.append(new_film)
    return new_film