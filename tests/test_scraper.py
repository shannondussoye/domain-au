import unittest
import pandas as pd
import os
import requests as re
from bs4 import BeautifulSoup
import json


url = "https://www.domain.com.au/rent/?excludedeposittaken=1&postcode=2000&page=1"

# test to read post code
class TestPostCodeFile(unittest.TestCase):
   def test_read_post_code(self):
       path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data','Post Codes.csv'))
       post_c = pd.read_csv(path, names=['postcode'])
       self.assertIsNotNone(post_c)
       self.assertEqual(post_c['postcode'][0], 800)
       self.assertEqual(post_c['postcode'][155], 2147)

# test request
class TestRequest(unittest.TestCase):
    def test_request(self):
        response = re.get(url)
        self.assertEqual(response.status_code,200)


class TestParser(unittest.TestCase):
    def test_request(self):
        html = re.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        js = soup.find_all('script')
        self.assertIsNotNone(js)
        for resultset in js:
            if str(resultset).startswith("<script>window.renderizrData = (window.renderizrData || {});"):
                js_data = str(resultset)
                js_data = js_data.replace(
                    "<script>window.renderizrData = (window.renderizrData || {}); window.renderizrData[\"page\"] = ",
                    " "). \
                    replace(";</script>", "").encode("utf-8").decode('utf-8', 'ignore').strip()

                self.assertIsNotNone(json.dumps(js_data))


# TODO: Write test for reading json data
# TODO: Write test for cleaning data
# TODO: Write test for connecting to db
# TODO: Write test to insert, retrieve and delete


if __name__ == '__name__':
    unittest.main()