import pytest
from garden_groups import garden_regions, explore_region

class Test_first_garden():
    data = (("A", "A", "A", "A"), 
            ("B", "B", "C", "D"), 
            ("B", "B", "C", "C"), 
            ("E", "E", "E", "C")) 

    regionB = [(1, 0), (1, 1), (2, 0), (2, 1)]
    regionC = [(1, 2), (2, 2), (2, 3), (3, 3)]

    @pytest.mark.skip(reason="not ready func")
    def test_simple_garden(self):
        assert garden_regions(self.data) == 140


    def test_region_in_simple_garder(self):
        assert explore_region(self.data, (1, 2)) == tuple(sorted(self.regionC))
