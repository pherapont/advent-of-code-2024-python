import unittest
from xmas_search import search_xmas, search_mas
from test_data import origin_data, horiz_overlap, simple_mas

class XmasSearchTest(unittest.TestCase):
    @unittest.skip("test for day 1")
    def test_xmas_search_origin_data(self):
        data = origin_data.split()
        self.assertEqual(search_xmas(data), 18)

    def test_mas_search_origin_data(self):
        data = origin_data.split()
        self.assertEqual(search_mas(data), 9)

    @unittest.skip("test for day 1")
    def test_horizontal_overlap(self):
        data = horiz_overlap.split()
        self.assertEqual(search_xmas(data), 3)

    def test_mas_simple_search(self):
        data = simple_mas.split()
        self.assertEqual(search_mas(data), 1)


if __name__ == '__main__':
    unittest.main()
