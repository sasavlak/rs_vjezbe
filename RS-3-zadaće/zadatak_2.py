import asyncio

async def dohvati_korisnike():
    print("Dohvaćanje podataka o korisnicima...")
    await asyncio.sleep(3)
    korisnici = [
        {"id": 1, "ime": "Ana"},
        {"id": 2, "ime": "Marko"},
        {"id": 3, "ime": "Ivana"}
    ]
    print("Podaci o korisnicima dohvaćeni.")
    return korisnici
async def dohvati_proizvode():
    print("Dohvaćanje podataka o proizvodima...")
    await asyncio.sleep(5) 
    proizvodi = [
        {"id": 101, "naziv": "Laptop"},
        {"id": 102, "naziv": "Mobitel"},
        {"id": 103, "naziv": "Tablet"}
    ]
    print("Podaci o proizvodima dohvaćeni.")
    return proizvodi
async def main():
    print("Početak dohvaćanja podataka...")
    korisnici, proizvodi = await asyncio.gather(dohvati_korisnike(), dohvati_proizvode())
    print("Svi podaci su dohvaćeni!")
    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)
asyncio.run(main())