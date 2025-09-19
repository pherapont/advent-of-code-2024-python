import unittest
from correct_updates import (parser_data, finalize_rules,
                             divide_updates,
                             correction_updates,
                             transform_updates, main)

class TestCorrectUpdates(unittest.TestCase):
    def test_correct_update_data_from_site(self):
        self.assertEqual(main("test_data.txt")[0], 143)

    def test_corrected_update_data_from_site(self):
        self.assertEqual(main("test_data.txt")[1], 123)

    @unittest.skip("local test")
    def test_parser_data(self):
        rules = ["1|1", "2|2", "133|585"]
        updates = ["22 33 44", "75 43 21", "85 49 32 45"]
        self.assertEqual(parser_data("test_parser_data.txt"),
                         (rules, updates))

    @unittest.skip("local test")
    def test_transform_updates(self):
        row_updates = ["22,33,44", "75,43,21", "85,49,32,45"]
        updates = [[22, 33, 44], [75, 43, 21], [85, 49, 32, 45]]
        self.assertEqual(transform_updates(row_updates), updates)

    @unittest.skip("local test")
    def test_finalize_rules(self):
        row_rules = ["1|1", "14|1", "21|2", "2|2", "133|585"]
        rules = {1: {1, 14}, 2: {21, 2}, 585: {133}}
        self.assertEqual(finalize_rules(row_rules), rules)

    @unittest.skip("local test")
    def test_divide_updates(self):
        rules = {2: {1}, 8: {1, 2}, 14: {1, 2, 8}}
        updates = [[1, 2, 8, 14], [2, 1, 8], [2, 14], [14, 1]]
        correct_updates = [[1, 2, 8, 14], [2, 14]]
        uncorrect_updates = [[2, 1, 8], [14, 1]]
        self.assertEqual(divide_updates(updates, rules),
                         (correct_updates, uncorrect_updates))

    @unittest.skip("local test")
    def test_correction_udates(self):
        rules = {2: {1}, 8: {1, 2}, 14: {1, 2, 8}}
        updates = [[1, 8, 14, 2], [2, 1, 8], [14, 2, 1], [14, 8]]
        corrected = [[1, 2, 8, 14], [1, 2, 8], [1, 2, 14], [8, 14]]
        self.assertEqual(correction_updates(updates, rules),
                         corrected)



if __name__ == '__main__':
    unittest.main()
