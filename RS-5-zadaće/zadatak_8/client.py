import aiohttp
import asyncio

async def fetch_cat_facts(amount):
    url = f'http://localhost:8086/cats?amount={amount}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def filter_cat_facts(facts):
    url = 'http://localhost:8087/facts'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"facts": facts}) as response:
            return await response.json()

async def main():
    print("Dohvaćam činjenice o mačkama...")
    cat_facts_response = await fetch_cat_facts(amount=10)
    cat_facts = cat_facts_response.get("facts", [])
    print("Činjenice o mačkama:", cat_facts)

    print("Filtriram činjenice...")
    filtered_facts_response = await filter_cat_facts(cat_facts)
    filtered_facts = filtered_facts_response.get("filtered_facts", [])
    print("Filtrirane činjenice:", filtered_facts)

if __name__ == '__main__':
    asyncio.run(main())