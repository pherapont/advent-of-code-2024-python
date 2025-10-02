import unittest

from true_clibrations import check_calibration


class TestCalibratons(unittest.TestCase):
    def test_check_trues_clibration(self):
        nums = (2, 5, 11)
        res = 21
        self.assertTrue(check_calibration(nums, res))

    def test_check_false_calibration(self):
        nums = (2, 5, 11)
        res = 20
        self.assertFalse(check_calibration(nums, res))

if __name__ == "__main__":
    unittest.main()
