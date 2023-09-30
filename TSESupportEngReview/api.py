import aiohttp
import asyncio
import time

start_time = time.time()

async def get_pokemon(session, url):
    async with session.get(url, auth=aiohttp.BasicAuth('quevin.bambasi@color.com', '')) as resp:
        pokemon = await resp.json()
        return pokemon['total']

async def main():
    async with aiohttp.ClientSession() as session:
        endpoint = 'https://getcolor.atlassian.net/rest/api/2/search?'
        jql = (
            'jql=resolved%20>%3D%202023-08-01%20' + 'AND' +
            '%20resolved%20<%3D%202023-09-01%20' + 'AND' +
            '%20project%20%3D%20SUPPORT%20' + 'AND' +
            '%20status%20in%20(DONE%2C%20Done)%20' + 'AND' +
            '%20priority%20in%20("P2%20(Medium)"%2C%20"P3%20(Low)"%2C%20"P4%20(Lowest)")' +
            '%20order%20by%20created%20DESC'
        )

        tasks = []
        for number in range(1, 100):
            pokemon_url = endpoint + jql
            tasks.append(asyncio.ensure_future(get_pokemon(session, pokemon_url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
              print(pokemon)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))