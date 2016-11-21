import sys
import asyncio
import aiohttp
from tornado import ioloop


async def fetch_page(client, url, n):
    response = await client.get(url)
    async with response:
        body = await response.read()
        print(n, response.status, len(body))


async def main():
    client = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=500, force_close=True))
    for n in range(0, 10):
        await fetch_page(client, 'http://www.yahoo.com/', n)
    client.close()


print(sys.version_info, '+ aiohttp', aiohttp.__version__)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
