import unittest

from guard_in_room import data_preparation


class TestGuardInRoom(unittest.TestCase):
    def test_data_preparation(self):
        data_struct = [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
        ]
        init_pos = [2, 2]
        self.assertEqual(
            data_preparation("data_preparation_test.txt"), (data_struct, init_pos)
        )


if __name__ == "__main__":
    unittest.main()
