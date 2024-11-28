import asyncio

async def dohvati_podatke():
    print("Dohvaćanje podataka...")
    await asyncio.sleep(3)
    podaci = [x for x in range(1, 11)] 
    print("Podaci dohvaćeni.")
    return podaci
async def main():
    podaci = await dohvati_podatke() 
    print("Dohvaćeni podaci:", podaci)
asyncio.run(main())