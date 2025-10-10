import unittest

from disk_fragmenter import (
    defragment_disk,
    get_check_sum,
    get_data_from_file,
    get_disk_map,
    main,
)


class TestDiskFragmenter(unittest.TestCase):
    def test_get_simple_disk_map(self):
        disk_desc = (1, 2, 3, 4, 5)
        disk_map = (0, -1, -1, 1, 1, 1, -1, -1, -1, -1, 2, 2, 2, 2, 2)
        self.assertEqual(get_disk_map(disk_desc), disk_map)

    def test_get_data_from_simple_file(self):
        self.assertEqual(get_data_from_file("data_simple_test.txt"), (1, 2, 3, 4, 5))

    def test_defragment_simple_disk(self):
        disk_map = (0, -1, -1, 1, 1, 1, -1, -1, -1, -1, 2, 2, 2, 2, 2)
        res = (0, 2, 2, 1, 1, 1, 2, 2, 2)
        self.assertEqual(defragment_disk(disk_map), res)

    def test_get_simple_checksum(self):
        disk = (0, 2, 2, 1, 1, 1, 2, 2, 2)
        res = 60
        self.assertEqual(get_check_sum(disk), res)

    def test_complex_simple_input(self):
        self.assertEqual(main("data_simple_test.txt"), 60)

    def test_complex_second_input(self):
        self.assertEqual(main("data_second_test.txt"), 1928)


if __name__ == "__main__":
    unittest.main()
