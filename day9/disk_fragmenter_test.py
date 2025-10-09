import unittest
from disk_fragmenter import get_disk_map, get_data_from_file

class TestDiskFragmenter(unittest.TestCase):
    def test_get_simple_disk_map(self):
        disk_desc = (1, 2, 3, 4, 5)
        map = (0, -1, -1, 1, 1, 1, -1, -1, -1, -1, 2, 2, 2, 2, 2)
        self.assertEqual(get_disk_map(disk_desc), map)

    def test_get_data_from_simple_file(self):
        self.assertEqual(get_data_from_file("data_simple_test.txt"),
                         (1, 2, 3, 4, 5))

if __name__ == "__main__":
    unittest.main()
