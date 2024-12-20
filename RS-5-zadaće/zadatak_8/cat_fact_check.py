from aiohttp import web

async def check_facts(request):
    try:
        data = await request.json()
        facts = data.get("facts", [])
        filtered_facts = [fact for fact in facts if "cat" in fact.lower()]
        return web.json_response({"filtered_facts": filtered_facts})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)

app = web.Application()
app.router.add_post('/facts', check_facts)

if __name__ == '__main__':
    web.run_app(app, port=8087)