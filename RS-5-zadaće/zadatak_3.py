from aiohttp import web

korisnici = [
    {'ime': 'Ivo', 'godine': 25},
    {'ime': 'Ana', 'godine': 17},
    {'ime': 'Marko', 'godine': 19},
    {'ime': 'Maja', 'godine': 16},
    {'ime': 'Iva', 'godine': 22}
]

async def get_punoljetni(request):
    punoljetni = [korisnik for korisnik in korisnici if korisnik['godine'] > 18]
    return web.json_response(punoljetni)

def main():
    app = web.Application()
    app.router.add_get('/punoljetni', get_punoljetni)
    web.run_app(app, port=8082)

if __name__ == "__main__":
    main()
