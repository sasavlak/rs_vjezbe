from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

# Kreiramo FastAPI aplikaciju
app = FastAPI()

# Pydantic model za automobil
class Automobil(BaseModel):
    id: int
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str

# Baza podataka sa primjerima automobila
automobili = [
    Automobil(id=1, marka="Toyota", model="Corolla", godina_proizvodnje=2020, cijena=15000.0, boja="crvena"),
    Automobil(id=2, marka="Volkswagen", model="Golf", godina_proizvodnje=2018, cijena=12000.0, boja="plava"),
    Automobil(id=3, marka="BMW", model="320d", godina_proizvodnje=2021, cijena=30000.0, boja="bijela"),
    Automobil(id=4, marka="Ford", model="Focus", godina_proizvodnje=2015, cijena=10000.0, boja="crna"),
    Automobil(id=5, marka="Audi", model="A4", godina_proizvodnje=2019, cijena=25000.0, boja="siva"),
]

# Ruta za dohvaćanje automobila prema ID i filtriranje sa query parametrima
@app.get("/automobili", response_model=List[Automobil])
def get_automobili(
    min_cijena: Optional[float] = Query(default=0.0, ge=0.01, description="Minimalna cijena automobila (mora biti > 0)"),
    max_cijena: Optional[float] = Query(default=None, description="Maksimalna cijena automobila"),
    min_godina: Optional[int] = Query(default=1960, ge=1960, description="Minimalna godina proizvodnje (mora biti > 1960)"),
    max_godina: Optional[int] = Query(default=None, description="Maksimalna godina proizvodnje")
):
    # Validacija nelogičnih parametara
    if max_cijena is not None and min_cijena > max_cijena:
        raise HTTPException(status_code=400, detail="Minimalna cijena ne može biti veća od maksimalne cijene.")
    
    if max_godina is not None and min_godina > max_godina:
        raise HTTPException(status_code=400, detail="Minimalna godina proizvodnje ne može biti veća od maksimalne godine proizvodnje.")

    # Filtriranje automobila prema parametrima
    filtrirani_automobili = [
        automobil for automobil in automobili
        if (min_cijena <= automobil.cijena <= (max_cijena if max_cijena is not None else float("inf")))
        and (min_godina <= automobil.godina_proizvodnje <= (max_godina if max_godina is not None else float("inf")))
    ]

    # Ako nema automobila koji zadovoljavaju filter prazan popis
    return filtrirani_automobili
