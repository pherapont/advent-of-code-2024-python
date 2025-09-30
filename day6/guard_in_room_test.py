import unittest

from guard_in_room import data_preparation, room_tour


class TestGuardInRoom(unittest.TestCase):
    def setUp(self):
        self.data_struct = [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
        ]
        self.init_pos = [2, 2]

    def test_data_preparation(self):
        self.assertEqual(
            data_preparation("data_preparation_test.txt"),
            (self.data_struct, self.init_pos),
        )

    def test_little_room_toor(self):
        self.assertEqual(room_tour(self.data_struct, self.init_pos), 7)


if __name__ == "__main__":
    unittest.main()
