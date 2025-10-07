import unittest
from antinodes_search import check_nodes, search_antinodes


class AntinodesTest(unittest.TestCase):
    @unittest.skip("later")
    def test_check_simple_nodes(self):
        map = [
            [".", ".", ".", "."],
            [".", "0", ".", "."],
            [".", ".", "0", "."],
            [".", ".", ".", "."],
        ]
        res = {[0, 0], [3, 3]}
        self.assertEqual(check_nodes(map), res)

    def test_search_simple_antinodes(self):
        nodes = [(1, 1), (2, 2)]
        field_size = (4, 4)
        res = {(0, 0), (3, 3)}
        self.assertEqual(search_antinodes(nodes, field_size), res)

    def test_horisontal_nodes(self):
        nodes = [(1, 1), (1, 2)]
        field_size = (4, 4)
        res = {(1, 0), (1, 3)}
        self.assertEqual(search_antinodes(nodes, field_size), res)

    def test_vertical_nodes(self):
        nodes = [(1, 1), (2, 1)]
        field_size = (4, 4)
        res = {(0, 1), (3, 1)}
        self.assertEqual(search_antinodes(nodes, field_size), res)

    def test_three_nodes(self):
        nodes = [(3, 4), (4, 8), (5, 5)]
        field_size = (9, 9)
        res = {(1, 3), (2, 0), (6, 2), (7, 6)}
        self.assertEqual(search_antinodes(nodes, field_size), res)

if __name__ == "__main__":
    unittest.main()
