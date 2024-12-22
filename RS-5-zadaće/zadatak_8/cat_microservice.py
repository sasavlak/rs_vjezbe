from aiohttp import web
import aiohttp
import asyncio

async def fetch_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        return await response.json()

async def get_cats(request):
    try:
        amount = int(request.query.get('amount', 1))
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_cat_fact(session) for _ in range(amount)]
            facts = await asyncio.gather(*tasks)
            return web.json_response({"facts": [fact["fact"] for fact in facts]})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)

app = web.Application()
app.router.add_get('/cats', get_cats)

if __name__ == '__main__':
    web.run_app(app, port=8086)