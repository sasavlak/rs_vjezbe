import hashlib
import aiohttp
import asyncio
from aiohttp import web

# Lista korisnika 
korisnici = [
    {"korisnicko_ime": "admin", "lozinka_hash": "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"},  
    {"korisnicko_ime": "markoMaric", "lozinka_hash": "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"},  
    {"korisnicko_ime": "ivanHorvat", "lozinka_hash": "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"}, 
    {"korisnicko_ime": "Nada000", "lozinka_hash": "492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"} 
]

# Hashiranje lozinke
def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

# Registraciju korisnika
async def register(request):
    data = await request.json()
    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")
    
    if not korisnicko_ime or not lozinka:
        return web.json_response({"error": "Nedostaje korisničko ime ili lozinka"}, status=400)
    
    # Provjera postoji li korisnik
    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == korisnicko_ime:
            return web.json_response({"error": "Korisnik već postoji"}, status=400)
    
    # Dodavanje korisnika s hashiranom lozinkom
    korisnici.append({"korisnicko_ime": korisnicko_ime, "lozinka_hash": hash_data(lozinka)})
    return web.json_response({"message": "Korisnik uspješno registriran"}, status=201)

# Prijava korisnika
async def login(request):
    data = await request.json()
    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")
    
    if not korisnicko_ime or not lozinka:
        return web.json_response({"error": "Nedostaje korisničko ime ili lozinka"}, status=400)
    
    # Pronalaženje korisnika
    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == korisnicko_ime:
            if korisnik["lozinka_hash"] == hash_data(lozinka):
                return web.json_response({"message": "Prijava uspješna"}, status=200)
            else:
                return web.json_response({"error": "Neispravna lozinka"}, status=401)
    
    return web.json_response({"error": "Korisnik ne postoji"}, status=404)

app = web.Application()
app.router.add_post("/register", register)
app.router.add_post("/login", login)

if __name__ == "__main__":
    web.run_app(app, host='0.0.0.0', port=9000)
