import unittest

from antinodes_search import get_nodes_coordinates, main, search_antinodes


class AntinodesTest(unittest.TestCase):
    @unittest.skip("new rules, it's nessesary correct")
    def test_get_nodes_coordinates(self):
        map = [
            [".", ".", ".", "."],
            [".", "0", ".", "."],
            ["a", ".", "0", "."],
            [".", "a", ".", "."],
        ]
        node = "0"
        res = [(1, 1), (2, 2)]
        self.assertEqual(get_nodes_coordinates(map, node), res)

    def test_search_simple_antinodes(self):
        nodes = [(1, 1), (2, 2)]
        field_size = (4, 4)
        res = {(0, 0), (1, 1), (2, 2), (3, 3)}
        self.assertEqual(search_antinodes(nodes, field_size), res)

    def test_horisontal_nodes(self):
        nodes = [(1, 1), (1, 2)]
        field_size = (4, 4)
        res = {(1, 0), (1, 1), (1, 2), (1, 3)}
        self.assertEqual(search_antinodes(nodes, field_size), res)

    def test_vertical_nodes(self):
        nodes = [(1, 1), (2, 1)]
        field_size = (4, 4)
        res = {(0, 1), (1, 1), (2, 1), (3, 1)}
        self.assertEqual(search_antinodes(nodes, field_size), res)

    #TODO: этот тест не проходит частично. Ищем ошибку отсюда,

    def test_three_nodes(self):
        nodes = [(0, 0), (1, 3), (2, 1)]
        field_size = (10, 10)
        res = {(0, 0), (0, 5), (1, 3), (2, 1), (2, 6), (3, 9), (4, 2), (6, 3), (8, 4)}
        self.assertEqual(search_antinodes(nodes, field_size), res)

    @unittest.skip("new rules, it's nessesary correct")
    def test_data_first_test(self):
        res = 34
        self.assertEqual(main("data_first_test.txt"), res)


if __name__ == "__main__":
    unittest.main()
