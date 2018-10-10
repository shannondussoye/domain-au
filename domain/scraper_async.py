from aiohttp import ClientSession, TCPConnector
from pypeln import asyncio_task as aio
import pandas as pd
from bs4 import BeautifulSoup
import json
import re

list_data = []

# read Postcode Fileç
post_c = pd.read_csv('../data/Post Codes.csv', names=['postcode'])
post_i = iter(post_c['postcode'].tolist())
urls = ("https://www.domain.com.au/rent/?excludedeposittaken=1&postcode={}&page=1".format(i) for i in post_i)


async def html_parser(html):
    if str(html) != "None":
        print("Parsing Html!")
        soup = BeautifulSoup(html, "html.parser")
        js = soup.find_all('script')
        for resultset in js:
            if str(resultset).startswith("<script>window.renderizrData = (window.renderizrData || {});"):
                js_data = str(resultset)
                js_data = js_data.replace(
                    "<script>window.renderizrData = (window.renderizrData || {}); window.renderizrData[\"page\"] = ",
                    " "). \
                    replace(";</script>", "").encode("utf-8").decode('utf-8', 'ignore').strip()
                list_data.append(js_data)
                if 'totalPages' in json.loads(js_data):
                    pages = ((json.loads(js_data)['totalPages']) + 1)
                else:
                    pages = 0
            else:
                continue
        return pages
    else:
        return 0


async def fetch(url, session):
    async with session.get(url) as response:
        print("Request")
        raw_html = await response.read()
        page_i = await html_parser(raw_html)
        if page_i > 2:
            for url_i in range(2, page_i):
                n_p_url = str(re.sub(r'page=\d{1,}', 'page=' + str(url_i), url))
                async with session.get(n_p_url) as n_response:
                    print("Sub Request")
                    raw_html2 = await n_response.read()
                    await  html_parser(raw_html2)


def write():
    print('Finished Scraping. Writing File:')
    json_data = json.dumps(list_data)
    file = open('../data/data_async.json', 'w')
    file.write(json_data)


def main():
    aio.each(
        fetch,
        urls,
        workers=1000,
        on_start=lambda: ClientSession(connector=TCPConnector(verify_ssl=False)),
        on_done=lambda _status, session: session.close(),
        run=True,
    )
    write()


if __name__ == "__main__":
    main()
