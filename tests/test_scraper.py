import unittest
import pandas as pd

# read csv
class TestAdvancedGet(unittest.TestCase):
    def test_advanced_get(self):
        post_c = pd.read_csv('data/Post Codes.csv', names=['postcode'])
        self.assertIsNotNone(post_c)
        self.assertEqual(post_c['postcode'][0],800)
        self.assertEqual(post_c['postcode'][155], 2147)

# TODO: Write test for reading json data
# TODO: Write test for cleaning data
# TODO: Write test for connecting to db
# TODO: Write test to insert, retrieve and delete


if __name__ == '__name__':
    unittest.main()