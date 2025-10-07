import unittest

from antinodes_search import check_nodes, search_antinodes


class AntinodesTest(unittest.TestCase):
    def test_check_simple_nodes(self):
        map = [
            [".", ".", ".", "."],
            [".", "0", ".", "."],
            [".", ".", "0", "."],
            [".", ".", ".", "."],
        ]
        res = [[0, 0], [3, 3]]
        self.assertEqual(check_nodes(map), res)

    def test_search_simple_antinodes(self):
        nodes = [(1, 1), (2, 2)]
        field_size = (4, 4)
        res = [[0, 0], [3, 3]]
        self.assertEqual(search_antinodes(nodes, field_size), res)


if __name__ == "__main__":
    unittest.main()
