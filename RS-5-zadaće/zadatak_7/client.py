import aiohttp
import asyncio

async def posalji_zahtjev(url, payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            return await response.json()

async def main():
    payload = {"brojevi": [1, 2, 3, 4]}

    # Konkurentno pozivanje prvog i drugog mikroservisa
    print("Pokrećem prva dva mikroservisa...")
    task1 = posalji_zahtjev('http://localhost:8083/zbroj', payload)
    task2 = posalji_zahtjev('http://localhost:8084/umnozak', payload)
    odgovori = await asyncio.gather(task1, task2)

    zbroj_rezultat = odgovori[0].get("zbroj")
    umnozak_rezultat = odgovori[1].get("umnozak")
    print("Zbroj:", zbroj_rezultat)
    print("Umnožak:", umnozak_rezultat)

    # Sekvencijalno pozivanje trećeg mikroservisa
    print("Pokrećem treći mikroservis...")
    kolicnik_rezultat = await posalji_zahtjev('http://localhost:8085/kolicnik', {
        "zbroj": zbroj_rezultat,
        "umnozak": umnozak_rezultat
    })
    print("Količnik:", kolicnik_rezultat)

if __name__ == '__main__':
    asyncio.run(main())