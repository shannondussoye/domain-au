import pandas as pd
import re
from bs4 import BeautifulSoup
import json
import simpleget as get

# Declarations
base_url = 'https://www.domain.com.au/rent/?excludedeposittaken=1&postcode=800&page=1'

list_data = []

""" Read Post Code File, Loop through postcode."""


def scrape():
    print('Starting Scraping')
    post_c = pd.read_csv('../data/Post Codes.csv', names=['postcode'])
    for index, row in post_c.iterrows():
        sub_p_code = 'postcode=' + str(row['postcode'])
        n_url = re.sub(r'postcode=\d{3,}', sub_p_code, base_url)
        n_pages = advanced_get(n_url)
        print(n_pages)
        if n_pages > 2:
            for i in range(2, n_pages):
                n_p_url = re.sub(r'page=\d{1,}', 'page=' + str(i), n_url)
                advanced_get(n_p_url)


def advanced_get(url):
    raw_html = get.simple_get(url)
    print('Scraping page: ' + url)
    if str(raw_html) != "None":
        soup = BeautifulSoup(raw_html, "html.parser")
        js = soup.find_all('script')
        for resultset in js:
            if str(resultset).startswith("<script>window.renderizrData = (window.renderizrData || {});"):
                js_data = str(resultset)
                js_data = js_data.replace(
                    "<script>window.renderizrData = (window.renderizrData || {}); window.renderizrData[\"page\"] = ",
                    " "). \
                    replace(";</script>", "").encode("utf-8").decode('utf-8', 'ignore').strip()
                list_data.append(js_data)
                pages = ((json.loads(js_data)['totalPages']) + 1)
            else:
                continue
        return pages
    else:
        return 0


def write():
    print('Finished Scraping. Writing File:')
    json_data = json.dumps(list_data)
    file = open('data.json', 'w')
    file.write(json_data)


def main():
    scrape()
    write()


if __name__ == "__main__":
    main()
