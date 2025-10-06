import unittest
from antinodes_search import search_anitnodes

class AntinodesTest(unittest.TestCase):

    def test_search_simple_antinodes(self):
        map = [[".", ".", ".", "."],
               [".", "0", ".", "."],
               [".", ".", "0", "."],
               [".", ".", ".", "."]]
        res = [[0, 0], [3, 3]]
        self.assertEqual(search_anitnodes(map), res)


if __name__ == '__main__':
    unittest.main()
