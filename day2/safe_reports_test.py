import unittest
from safe_reports import get_nums, check_report, check_light_report


class TestSafeReports(unittest.TestCase):

    def test_get_only_nums(self):
        data = "125 222 333 44"
        output = [125, 222, 333, 44]
        self.assertEqual(get_nums(data), output)

    def test_get_nums_with_whitspaces(self):
        data = "  125 222 333 44\t"
        output = [125, 222, 333, 44]
        self.assertEqual(get_nums(data), output)

    def test_check_safe_increase_report(self):
        data = [125, 126, 128, 131]
        self.assertTrue(check_report(data))

    def test_check_safe_decrease_report(self):
        data = [432, 430, 427, 426]
        self.assertTrue(check_report(data))

    def test_check_to_large_step_report(self):
        data = [1, 10, 20]
        self.assertFalse(check_report(data))

    def test_check_null_step_report(self):
        data = [10, 10]
        self.assertFalse(check_report(data))

    def test_check_safe_light_report(self):
        data = [10, 9, 11, 14]
        self.assertTrue(check_light_report(data))

    def test_check_safe_light_report_with_equal(self):
        data = [22, 22, 24, 29]
        self.assertFalse(check_light_report(data))

    def test_check_light_report_unsafe(self):
        data = [33, 37, 42, 43]
        self.assertFalse(check_light_report(data))

if __name__ == '__main__':
    unittest.main()
