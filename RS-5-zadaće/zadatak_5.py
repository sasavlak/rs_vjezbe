from aiohttp import web, ClientSession 

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def get_proizvod_by_id(request):
    try:
        proizvod_id = int(request.match_info['id'])
        
        proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)
        
        if proizvod:
            return web.json_response(proizvod)
        else:
            return web.json_response({"error": "Proizvod s traženim ID-em ne postoji"}, status=404)
    except ValueError:
        return web.json_response({"error": "Neispravan ID"}, status=400)

async def post_narudzbe(request):
    try:
        nova_narudzba = await request.json()
        proizvod_id = nova_narudzba.get("proizvod_id")
        kolicina = nova_narudzba.get("kolicina")

        proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)

        if not proizvod:
            return web.json_response({"error": "Proizvod s traženim ID-em ne postoji"}, status=404)

        narudzba = {"proizvod_id": proizvod_id, "kolicina": kolicina}
        narudzbe.append(narudzba)

        return web.json_response(narudzbe, status=201)
    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)

async def main():
    app = web.Application()
    
    app.router.add_get('/proizvodi', get_proizvodi)
    app.router.add_get('/proizvodi/{id}', get_proizvod_by_id)
    app.router.add_post('/narudzbe', post_narudzbe)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()

    print("Poslužitelj radi na http://localhost:8081")

    async with ClientSession() as session:  
        try:
            async with session.get('http://localhost:8081/proizvodi') as resp:
                print("/proizvodi status:", resp.status)
                print("/proizvodi odgovor:", await resp.json())

            async with session.get('http://localhost:8081/proizvodi/1') as resp:
                print("/proizvodi/1 status:", resp.status)
                print("/proizvodi/1 odgovor:", await resp.json())

            async with session.get('http://localhost:8081/proizvodi/99') as resp:
                print("/proizvodi/99 status:", resp.status)
                print("/proizvodi/99 odgovor:", await resp.json())

            async with session.post('http://localhost:8081/narudzbe', json={"proizvod_id": 1, "kolicina": 2}) as resp:
                print("/narudzbe status:", resp.status)
                print("/narudzbe odgovor:", await resp.json())

            async with session.post('http://localhost:8081/narudzbe', json={"proizvod_id": 99, "kolicina": 2}) as resp:
                print("/narudzbe (nepostojeći proizvod) status:", resp.status)
                print("/narudzbe (nepostojeći proizvod) odgovor:", await resp.json())
        except Exception as e:
            print("Greška tijekom HTTP zahtjeva:", str(e))

if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.create_task(main())
        loop.run_forever()
