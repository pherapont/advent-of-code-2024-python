import unittest

from true_clibrations import check_calibration, main, create_token_tree


class TestCalibratons(unittest.TestCase):
    def test_check_trues_clibration(self):
        nums = (2, 5, 11)
        res = 21
        operators = ("+", "*")
        tree = create_token_tree(nums, operators)
        self.assertTrue(check_calibration(tree, res))

    def test_check_false_calibration(self):
        nums = (2, 5, 11)
        operators = ("+", "*")
        res = 20
        tree = create_token_tree(nums, operators)
        self.assertFalse(check_calibration(tree, res))

    def test_data_from_site(self):
        self.assertEqual(main("data_main_test.py"), 3749)

if __name__ == "__main__":
    unittest.main()
