import pytest
from garden_groups import (explore_garden, explore_region,
                         bounds_count, region_cost, get_garden, main,
                        sides_count)

class Test_first_garden():

    @pytest.mark.skip("First part")
    class TestFirstPart:
        data = (("A", "A", "A", "A"), 
                ("B", "B", "C", "D"), 
                ("B", "B", "C", "C"), 
                ("E", "E", "E", "C")) 

        regionB = [(1, 0), (1, 1), (2, 0), (2, 1)]
        regionC = [(1, 2), (2, 2), (2, 3), (3, 3)]
        regionD = [ (1, 1), (1, 2), (1, 3),
                    (2, 1),         (2, 3),
                    (3, 1), (3, 2), (3, 3)]

        def test_simple_garden(self):
            assert explore_garden(self.data) == 140

        def test_region_C_in_simple_garden(self):
            assert explore_region(self.data, [], (1, 2),
                        "C") == tuple(sorted(self.regionC))

        def test_region_B_in_simple_garden(self):
            assert explore_region(self.data, [], (1, 0),
                        "B") == tuple(sorted(self.regionB))

        def test_region_B_bounds_count(self):
            assert bounds_count(self.regionB) == 4

        def test_region_C_bounds_count(self):
            assert bounds_count(self.regionC) == 6

        def test_region_D_bounds_count(self):
            assert bounds_count(self.regionD) == 8  

        def test_region_B_cost(self):
            assert region_cost(self.regionB) == 32

        def test_region_C_cost(self):
            assert region_cost(self.regionC) == 40

        def test_region_D_cost(self):
            assert region_cost(self.regionD) == 128

        def test_get_garden(self):
            assert get_garden("simple_input.txt") == self.data

        def test_main_simple_file(self):
            assert main("simple_input.txt") == 140

        def test_main_middle_file(self):
            assert main("middle_input.txt") == 1930

    class TestSecondPart:
        regionB = [(1, 0), (1, 1), (2, 0), (2, 1)]
        regionC = [(1, 2), (2, 2), (2, 3), (3, 3)]
        regionD = [ (1, 1), (1, 2), (1, 3),
                    (2, 1),         (2, 3),
                    (3, 1), (3, 2), (3, 3)]

        def test_regionB_sides_count(self):
            assert sides_count(self.regionB) == 2

        def test_regionC_sides_count(self):
            assert sides_count(self.regionC) == 4

        def test_regionD_sides_count(self):
            assert sides_count(self.regionD) == 4

        def test_main_simple_file(self):
            assert main("simple_input.txt") == 80

        def test_main_middle_file(self):
            assert main("middle_input.txt") == 1206
