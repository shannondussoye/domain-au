import unittest
import pandas as pd
import os

# test to read post code
class TestPostCodeFile(unittest.TestCase):
   def test_read_post_code(self):
       path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data','Post Codes.csv'))
       post_c = pd.read_csv(path, names=['postcode'])
       self.assertIsNotNone(post_c)
       self.assertEqual(post_c['postcode'][0], 800)
       self.assertEqual(post_c['postcode'][155], 2147)


# TODO: Write test for reading json data
# TODO: Write test for cleaning data
# TODO: Write test for connecting to db
# TODO: Write test to insert, retrieve and delete


if __name__ == '__name__':
    unittest.main()