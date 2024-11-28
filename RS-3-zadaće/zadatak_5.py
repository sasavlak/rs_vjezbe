import asyncio

async def secure_data(podaci):
    print(f"Pokrećem enkripciju za: {podaci['prezime']}...")
    await asyncio.sleep(3) 
    enkriptirani_podaci = {
        'prezime': podaci['prezime'],
        'broj_kartice': hash(podaci['broj_kartice']),
        'CVV': hash(podaci['CVV'])
    }
    print(f"Enkripcija završena za: {podaci['prezime']}")
    return enkriptirani_podaci

async def main():
    podaci_lista = [
        {'prezime': 'Horvat', 'broj_kartice': '1234567812345678', 'CVV': '123'},
        {'prezime': 'Kovačić', 'broj_kartice': '9876543298765432', 'CVV': '456'},
        {'prezime': 'Perić', 'broj_kartice': '5555555555554444', 'CVV': '789'}
    ]
    
    zadaci = [secure_data(podaci) for podaci in podaci_lista]
    
    rezultati = await asyncio.gather(*zadaci)
    
    print("Enkriptirani podaci:")
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())
