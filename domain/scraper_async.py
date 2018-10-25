import pandas as pd
from aiohttp import ClientSession, TCPConnector
from pypeln import asyncio_task as aio
from bs4 import BeautifulSoup
import json
import aiofiles

# Read Post Code File
post_c = pd.read_csv('../data/Post Codes.csv', names=['postcode'])

# Convert Post Code to generator
post_i = iter(post_c['postcode'].tolist())

# Create Url generator using Post Code
urls = ("https://www.domain.com.au/rent/?excludedeposittaken=1&postcode={}&page=1".format(i) for i in post_i)

limit = 100
list_data = []
multi_pages = []



async def fetch(url, session):
    print("Scraping: " + url)
    async with session.get(url) as response:
        raw_data = await response.read()
        if response.status == 200:
            await parse(url, raw_data)


async def parse(url, html):
    if str(html) != "None":
        print("Parsing Html!"+url)
        soup = BeautifulSoup(html, "html.parser")
        js = soup.find_all('script')
        for resultset in js:
            if str(resultset).startswith("<script>window.renderizrData = (window.renderizrData || {});"):
                js_data = str(resultset)
                js_data = js_data.replace(
                    "<script>window.renderizrData = (window.renderizrData || {}); window.renderizrData[\"page\"] = ",
                    " "). \
                    replace(";</script>", "").encode("utf-8").decode('utf-8', 'ignore').strip()

                json_data = (json.dumps(js_data))
                async with aiofiles.open('../data/data.json', 'w+') as file:
                    await file.write(json_data)

                if 'totalPages' in json.loads(js_data):
                    pages = ((json.loads(js_data)['totalPages']) + 1)
                    sub_pages_url = [n for n in range(2, pages)]
                    n_url = url.replace("&page=1", "&page={}")
                    nurls = list(n_url.format(i) for i in sub_pages_url)
                    await append(nurls)


async def append(l):
    multi_pages.append(l)



aio.each(
    fetch,
    urls,
    workers=limit,
    on_start=lambda: ClientSession(connector=TCPConnector(limit=None, verify_ssl=False)),
    on_done=lambda _status, session: session.close(),
    run=True,
)

flat_multi_pages = [item for sublist in multi_pages for item in sublist]
multi_p_url = iter(flat_multi_pages)

aio.each(
    fetch,
    multi_p_url,
    workers=limit,
    on_start=lambda: ClientSession(connector=TCPConnector(limit=None, verify_ssl=False)),
    on_done=lambda _status, session: session.close(),
    run=True,
)
