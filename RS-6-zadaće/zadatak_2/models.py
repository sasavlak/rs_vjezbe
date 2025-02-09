from pydantic import BaseModel

class Film(BaseModel):
    id: int
    naziv: str
    genre: str
    godina: int
