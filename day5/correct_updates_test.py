import unittest
from correct_updates import parser_data, finalize_rules

class TestCorrectUpdates(unittest.TestCase):
    @unittest.skip("for finish")
    def test_correct_update_data_from_site(self):
        self.assetEqual()

    def test_parser_data(self):
        rules = ["1|1", "2|2", "133|585"]
        updates = ["22 33 44", "75 43 21", "85 49 32 45"]
        self.assertEqual(parser_data("test_parser_data.txt"),
                         (rules, updates))

    def test_finalize_rules(self):
        row_rules = ["1|1", "14|1", "21|2", "2|2", "133|585"]
        rules = {"1": {"1", "14"}, "2": {"21", "2"}, "585": {"133"}}
        self.assertEqual(finalize_rules(row_rules), rules)

if __name__ == '__main__':
    unittest.main()
