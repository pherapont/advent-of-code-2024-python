import unittest
from xmas_search import search_xmas
from test_data import origin_data, horiz_overlap

class XmasSearchTest(unittest.TestCase):
    @unittest.skip("Finish testing")
    def test_origin_data(self):
        data = origin_data.split()
        self.assertEqual(search_xmas(data), 18)

    def test_horizontal_overlap(self):
        data = horiz_overlap.split()
        self.assertEqual(search_xmas(data), 3)


if __name__ == '__main__':
    unittest.main()
