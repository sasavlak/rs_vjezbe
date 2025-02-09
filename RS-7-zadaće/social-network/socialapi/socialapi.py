from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
import aiohttp

app = FastAPI()

objave = []

class NovaObjava(BaseModel):
    korisnik: str = Field(..., max_length=20)
    tekst: str = Field(..., max_length=280)

class Objava(NovaObjava):
    id: int
    vrijeme: datetime

class KorisnikLogin(BaseModel):
    korisnik: str
    lozinka: str

id_counter = 1

# Dodavanje nove objave
@app.post("/objava", response_model=Objava)
def dodaj_objavu(objava: NovaObjava):
    global id_counter
    nova_objava = Objava(id=id_counter, korisnik=objava.korisnik, tekst=objava.tekst, vrijeme=datetime.now())
    objave.append(nova_objava)
    id_counter += 1
    return nova_objava

# Ruta za dohvaćanje objave po ID
@app.get("/objava/{id}", response_model=Objava)
def dohvati_objavu(id: int):
    for objava in objave:
        if objava.id == id:
            return objava
    raise HTTPException(status_code=404, detail="Objava nije pronađena")

# Dohvaćanje svih objava
@app.post("/korisnici/{korisnik}/objave", response_model=List[Objava])
async def dohvati_objave_korisnika(korisnik: str, korisnik_login: KorisnikLogin):
    # Provjera korisnika 
    async with aiohttp.ClientSession() as session:
        async with session.post("http://authapi:9000/login",
                                json={"korisnicko_ime": korisnik_login.korisnik, "lozinka": korisnik_login.lozinka},
                                headers={"Content-Type": "application/json"}) as resp:
            auth_response = await resp.json()  
            if not auth_response.get("authenticated", False):
                raise HTTPException(status_code=401, detail="Neispravni korisnički podaci")

    korisnikove_objave = [objava for objava in objave if objava.korisnik == korisnik]
    if not korisnikove_objave:
        raise HTTPException(status_code=404, detail="Nema objava za ovog korisnika")
    
    return korisnikove_objave

# Pokretanje
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3500)
