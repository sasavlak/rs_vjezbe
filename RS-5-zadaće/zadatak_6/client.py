import aiohttp
import asyncio

async def posalji_zahtjev(url, port):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://{url}:{port}/pozdrav') as response:
            return await response.json()

async def main():
    print("Sekvencijalno slanje zahtjeva:")
    odgovor1 = await posalji_zahtjev('localhost', 8081)
    print("Odgovor od mikroservisa 1:", odgovor1)

    odgovor2 = await posalji_zahtjev('localhost', 8082)
    print("Odgovor od mikroservisa 2:", odgovor2)

    print("Konkurentno slanje zahtjeva:")
    tasks = [
        posalji_zahtjev('localhost', 8081),
        posalji_zahtjev('localhost', 8082)
    ]
    odgovori = await asyncio.gather(*tasks)
    for i, odgovor in enumerate(odgovori, start=1):
        print(f"Odgovor od mikroservisa {i}:", odgovor)

if __name__ == '__main__':
    asyncio.run(main())
