import unittest
from safe_reports import get_nums, check_report

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


if __name__ == '__main__':
    unittest.main()
