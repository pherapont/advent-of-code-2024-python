import unittest

from guard_in_room import data_preparation, room_tour, main


class TestGuardInRoom(unittest.TestCase):
    def setUp(self):
        self.data_struct = [
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
        ]
        self.init_pos = [2, 1]

    @unittest.skip("prepare test")
    def test_data_preparation(self):
        self.assertEqual(
            data_preparation("data_preparation_test.txt"),
            (self.data_struct, self.init_pos),
        )

    @unittest.skip("prepare test")
    def test_little_room_toor(self):
        self.assertEqual(room_tour(self.data_struct, self.init_pos), 8)

    def test_room_from_site(self):
        self.assertEqual(main('data_main_test.txt'), 41)

if __name__ == "__main__":
    unittest.main()
