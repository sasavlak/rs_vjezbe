from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional, Literal

# Model za glumca
class Actor(BaseModel):
    name: str
    surname: str

# Model za pisca
class Writer(BaseModel):
    name: str
    surname: str

# Model za film
class Film(BaseModel):
    Title: str
    Year: int = Field(ge=1900, description="Godina mora biti veća od 1900")
    Rated: str
    Released: str
    Runtime: int = Field(gt=0, description="Trajanje mora biti veće od 0")
    Genre: str
    Director: str
    Writer: str
    Actors: str
    Plot: str
    Language: str
    Country: str
    Awards: Optional[str]
    Poster: HttpUrl
    Metascore: Optional[int]
    imdbRating: float = Field(ge=0, le=10, description="IMDb ocjena mora biti između 0 i 10")
    imdbVotes: int = Field(gt=0, description="IMDb glasovi moraju biti veći od 0")
    imdbID: str
    Type: Literal["movie", "series"]
    Response: str
    Images: List[HttpUrl]

    class Config:
        schema_extra = {
            "example": {
                "Title": "Avatar",
                "Year": 2009,
                "Rated": "PG-13",
                "Released": "18 Dec 2009",
                "Runtime": 162,
                "Genre": "Action, Adventure, Fantasy",
                "Director": "James Cameron",
                "Writer": "James Cameron",
                "Actors": "Sam Worthington, Zoe Saldana, Sigourney Weaver",
                "Plot": "A paraplegic marine dispatched to the moon Pandora...",
                "Language": "English, Spanish",
                "Country": "USA, UK",
                "Awards": "Won 3 Oscars.",
                "Poster": "http://example.com/poster.jpg",
                "Metascore": 83,
                "imdbRating": 7.9,
                "imdbVotes": 890617,
                "imdbID": "tt0499549",
                "Type": "movie",
                "Response": "True",
                "Images": ["http://example.com/image1.jpg", "http://example.com/image2.jpg"]
            }
        }
