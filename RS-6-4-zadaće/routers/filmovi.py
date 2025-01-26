from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
from models.film_models import Film

router = APIRouter()

# Funkcije za obradu podataka
def process_runtime(runtime: str) -> int:
    """Pretvara '162 min' u 162. Ako format nije ispravan, vraća 1 kao minimalnu vrijednost."""
    try:
        return max(int(runtime.split()[0]), 1)  
    except (ValueError, AttributeError):
        return 1  # Zadana vrijednost ako je format neispravan

def process_votes(votes: str) -> int:
    """Pretvara '890,617' u 890617. Ako format nije ispravan, vraća 1 kao minimalnu vrijednost."""
    try:
        return max(int(votes.replace(",", "")), 1)  
    except (ValueError, AttributeError):
        return 1  # Zadana vrijednost ako je format neispravan

def process_year(year: str) -> int:
    """Pretvara '2011â€“' u 2011. Ako format nije ispravan, vraća 1900."""
    try:
        return int(year.split("â")[0])
    except (ValueError, AttributeError):
        return 1900  # Zadana vrijednost ako je format neispravan

def process_metascore(metascore: str) -> int:
    """Pretvara 'N/A' u 0."""
    try:
        return int(metascore) if metascore != "N/A" else 0
    except (ValueError, AttributeError):
        return 0  # Zadana vrijednost ako je format neispravan

def process_rating(rating: str) -> float:
    """Pretvara 'N/A' u 0.0."""
    try:
        return float(rating) if rating != "N/A" else 0.0
    except (ValueError, AttributeError):
        return 0.0  # Zadana vrijednost ako je format neispravan

# Učitavanje podataka iz JSON 
try:
    with open("Film.JSON", "r") as file:
        films_data = json.load(file)
    films = []
    for film in films_data:
        film["Runtime"] = process_runtime(film.get("Runtime", "0 min"))
        film["imdbVotes"] = process_votes(film.get("imdbVotes", "0"))
        film["Year"] = process_year(film.get("Year", "1900"))
        film["Metascore"] = process_metascore(film.get("Metascore", "N/A"))
        film["imdbRating"] = process_rating(film.get("imdbRating", "N/A"))
        films.append(Film(**film))
except FileNotFoundError:
    films = []

# Rute za API
@router.get("/filmovi", response_model=List[Film])
def get_all_movies(
    min_year: Optional[int] = Query(None, ge=1900),
    max_year: Optional[int] = Query(None, ge=1900),
    min_rating: Optional[float] = Query(None, ge=0, le=10),
    max_rating: Optional[float] = Query(None, ge=0, le=10),
    type: Optional[str] = Query(None, regex="^(movie|series)$")
):
    result = films
    if min_year is not None:
        result = [film for film in result if film.Year >= min_year]
    if max_year is not None:
        result = [film for film in result if film.Year <= max_year]
    if min_rating is not None:
        result = [film for film in result if film.imdbRating >= min_rating]
    if max_rating is not None:
        result = [film for film in result if film.imdbRating <= max_rating]
    if type is not None:
        result = [film for film in result if film.Type == type]
    return result

@router.get("/filmovi/{imdbID}", response_model=Film)
def get_movie_by_id(imdbID: str):
    for film in films:
        if film.imdbID == imdbID:
            return film
    raise HTTPException(status_code=404, detail="Film nije pronađen")

@router.get("/filmovi/naslov/{title}", response_model=Film)
def get_movie_by_title(title: str):
    for film in films:
        if film.Title.lower() == title.lower():
            return film
    raise HTTPException(status_code=404, detail="Film nije pronađen")
