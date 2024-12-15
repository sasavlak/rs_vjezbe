from aiohttp import web

proizvodi = [
    {"naziv": "Jabuka", "cijena": 3.5, "kolicina": 10},
    {"naziv": "Banana", "cijena": 2.0, "kolicina": 20},
    {"naziv": "Kruška", "cijena": 4.0, "kolicina": 15}
]

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def post_proizvodi(request):
    try:
        novi_proizvod = await request.json()

        print("Primljeni podaci:", novi_proizvod)

        proizvodi.append(novi_proizvod)

        return web.json_response(proizvodi)
    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)

def main():
    app = web.Application()
    app.router.add_get('/proizvodi', get_proizvodi)
    app.router.add_post('/proizvodi', post_proizvodi)
    web.run_app(app, port=8081)

if __name__ == "__main__":
    main()
