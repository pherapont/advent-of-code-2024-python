import unittest

from guard_in_room import data_preparation, find_all_cycles, is_cycle, main, room_tour


class TestGuardInRoom(unittest.TestCase):
    def setUp(self):
        self.data_struct = [
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
        ]
        self.init_pos = (2, 1)

    @unittest.skip("prepare test")
    def test_data_preparation(self):
        self.assertEqual(
            data_preparation("data_preparation_test.txt"),
            (self.data_struct, self.init_pos),
        )

    @unittest.skip("prepare test")
    def test_little_room_toor(self):
        self.assertEqual(room_tour(self.data_struct, self.init_pos), 8)

    @unittest.skip("first part")
    def test_room_from_site(self):
        self.assertEqual(main("data_main_test.txt"), 41)

    @unittest.skip("one cycle")
    def test_is_cycle_right(self):
        obstruction = [2, 0]
        self.assertTrue(is_cycle(self.data_struct, self.init_pos, obstruction))

    @unittest.skip("one cycle")
    def test_is_cycle_wrong(self):
        obstruction = [2, 2]
        self.assertFalse(is_cycle(self.data_struct, self.init_pos, obstruction))

    @unittest.skip("prepare")
    def test_all_points_for_cycle(self):
        visites = {(1, 2), (1, 3), (2, 3), (2, 2), (2, 1), (2, 0)}
        count_cycles = 0
        visites.discard(self.init_pos)
        for point in visites:
            res = is_cycle(self.data_struct, self.init_pos, point)
            count_cycles += res
        self.assertEqual(count_cycles, 1)

    def test_cycles_in_room_from_site(self):
        self.assertEqual(find_all_cycles("data_main_test.txt"), 6)


if __name__ == "__main__":
    unittest.main()
