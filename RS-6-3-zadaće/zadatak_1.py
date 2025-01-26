from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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
    Automobil(id=3, marka="BMW", model="320d", godina_proizvodnje=2021, cijena=30000.0, boja="bijela")
]

# Ruta za dohvaćanje podataka o automobilu prema ID
@app.get("/automobili/{automobil_id}", response_model=Automobil)
def get_automobil(automobil_id: int):
    for automobil in automobili:
        if automobil.id == automobil_id:
            return automobil
    
    raise HTTPException(status_code=404, detail="Automobil nije pronađen")
