from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Pydantic model
class BaseCar(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int = Field(ge=1960, description="Godina proizvodnje mora biti veća ili jednaka 1960.")
    boja: str

# Pydantic model za unos novog automobila 
class CarCreate(BaseCar):
    cijena: float = Field(ge=0.01, description="Cijena mora biti veća od 0.")

# Pydantic model za automobil s IDi cijenom s PDV
class CarOut(BaseCar):
    id: int
    cijena: float
    cijena_pdv: float

# Lista automobila
automobili: List[CarOut] = [
    CarOut(id=1, marka="Toyota", model="Corolla", godina_proizvodnje=2020, cijena=15000.0, cijena_pdv=18000.0, boja="crvena"),
    CarOut(id=2, marka="Volkswagen", model="Golf", godina_proizvodnje=2018, cijena=12000.0, cijena_pdv=14400.0, boja="plava"),
    CarOut(id=3, marka="BMW", model="320d", godina_proizvodnje=2021, cijena=30000.0, cijena_pdv=36000.0, boja="bijela")
]

# Funkcija za izračun cijene sa PDV
def izracunaj_cijenu_s_pdv(cijena: float, pdv_postotak: float = 20.0) -> float:
    return round(cijena * (1 + pdv_postotak / 100), 2)

# Ruta za dodavanje novog automobila
@app.post("/automobili", response_model=CarOut, status_code=201)
def dodaj_automobil(novi_automobil: CarCreate):
    # Provjera
    for automobil in automobili:
        if (
            automobil.marka == novi_automobil.marka and
            automobil.model == novi_automobil.model and
            automobil.godina_proizvodnje == novi_automobil.godina_proizvodnje and
            automobil.boja == novi_automobil.boja
        ):
            raise HTTPException(status_code=400, detail="Automobil već postoji u bazi podataka.")

    # Dodjela ID novom automobilu
    novi_id = max([automobil.id for automobil in automobili], default=0) + 1

    # Izračun cijene s PDV
    cijena_s_pdv = izracunaj_cijenu_s_pdv(novi_automobil.cijena)

    # Kreiranje novog automobila
    automobil = CarOut(
        id=novi_id,
        marka=novi_automobil.marka,
        model=novi_automobil.model,
        godina_proizvodnje=novi_automobil.godina_proizvodnje,
        cijena=novi_automobil.cijena,
        cijena_pdv=cijena_s_pdv,
        boja=novi_automobil.boja
    )

    # Dodavanje automobila u listu
    automobili.append(automobil)
    return automobil
