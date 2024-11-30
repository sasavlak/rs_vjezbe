import asyncio
import aiohttp

async def get_cat_fact():
    url = "https://catfact.ninja/fact"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data['fact']

async def filter_cat_facts(facts):
    filtered_facts = [fact for fact in facts if "cat" in fact.lower() or "cats" in fact.lower()]
    return filtered_facts

async def main():
    
    tasks = [get_cat_fact() for _ in range(20)]
    facts = await asyncio.gather(*tasks)  
    
    filtered_facts = await filter_cat_facts(facts)
    
    print("Filtrirane činjenice o mačkama:")
    for fact in filtered_facts:
        print(f"- {fact}")

if __name__ == "__main__":
    asyncio.run(main())
