import unittest

from disk_fragmenter import (
    get_disk_structure,
    DiskElem,
    defragment_disk_by_files,
    file_map,
    get_check_sum,
    main
)


class TestDiskFragmenter(unittest.TestCase):
    def setUp(self):
        self.disk_desc = (1, 3, 1, 4, 4)
        self.disk_structure =  [{"gap": 0, "el":1, "elems": [DiskElem(eid=0, esize=1)]},
                                {"gap": 3, "el":0, "elems": []},
                                {"gap": 0, "el":1, "elems": [DiskElem(eid=1, esize=1)]},
                                {"gap": 4, "el":0, "elems": []},
                                {"gap": 0, "el":4, "elems": [DiskElem(eid=2, esize=4)]}]
        self.defragm_struct = [{"gap": 0, "el":1, "elems": [DiskElem(eid=0, esize=1)]},
                          {"gap": 2, "el":1, "elems": [DiskElem(eid=1, esize=1)]},
                          {"gap": 1, "el":0, "elems": []},
                          {"gap": 0, "el":4, "elems": [DiskElem(eid=2, esize=4)]},
                          {"gap": 4, "el":0, "elems": []}]
        self.disk_map = (0, 1, -1, -1, -1, 2, 2, 2, 2, -1, -1, -1, -1)

    def test_get_disk_sturcture(self):
        self.assertEqual(get_disk_structure(self.disk_desc), self.disk_structure)

    def test_defragment_disk_by_files(self):
        self.assertEqual(defragment_disk_by_files(self.disk_structure), self.defragm_struct)

    def test_get_disk_map(self):
        self.assertEqual(file_map(self.defragm_struct), self.disk_map)

    def test_get_check_sum(self):
        self.assertEqual(get_check_sum(self.disk_map), 53)

    def test_simple_main(self):
        self.assertEqual(main("data_second_simple_test.txt"), 53)

    def test_data_from_site(self):
        self.assertEqual(main("data_second_test.txt"), 2858)

if __name__ == "__main__":
    unittest.main()
