import unittest

from true_clibrations import check_calibration, main, create_token_tree


class TestCalibratons(unittest.TestCase):
    def setUp(self):
        nums = ("2", "5", "11")
        operators = ("+", "*")
        self.tree = create_token_tree(nums, operators)

    def test_check_trues_clibration(self):
        res = "21"
        self.assertTrue(check_calibration(self.tree, res))

    def test_check_false_calibration(self):
        res = "20"
        self.assertFalse(check_calibration(self.tree, res))

    def test_data_from_site(self):
        self.assertEqual(main("data_main_test.py"), 11387)

if __name__ == "__main__":
    unittest.main()
