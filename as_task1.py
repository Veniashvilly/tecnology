import asyncio
import aiohttp
import time
urls = ["https://example.com"] * 10
async def async_http_get(url, session):
    async with session.get(url) as response:
        text = await response.text()
        return text

async def main():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [async_http_get(url, session) for url in urls]
        await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"time: {end_time - start_time:.2f} seconds")

asyncio.run(main())