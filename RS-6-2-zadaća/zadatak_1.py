from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Definicija Pydantic modela 
class Izdavac(BaseModel):
    naziv: str
    adresa: str

# Definicija Pydantic
class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: int = Field(default_factory=lambda: datetime.now().year)
    broj_stranica: int
    izdavac: Izdavac

if __name__ == "__main__":
    izdavac_podaci = {
        "naziv": "Moja Knjiga d.o.o.",
        "adresa": "Ulica knjiga 123, Zagreb"
    }

    knjiga_podaci = {
        "naslov": "Uvod u Python",
        "ime_autora": "Marko",
        "prezime_autora": "Marković",
        "broj_stranica": 250,
        "izdavac": izdavac_podaci 
    }

    # Validacija izdavača
    izdavac = Izdavac(**izdavac_podaci)
    print("Izdavač validiran:", izdavac)

    # Validacija knjige
    knjiga = Knjiga(**knjiga_podaci)
    print("Knjiga validirana:", knjiga)
