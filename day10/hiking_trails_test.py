from hiking_trails import get_trail_score, get_trail_map, main
from data_simple_test import t_map as simple_t_map
from data_middle_test import t_map as middle_t_map

def test_get_simple_trail_score():
    assert get_trail_score(simple_t_map, (0, 3)) == 2

def test_get_middle_trail_score():
    assert get_trail_score(middle_t_map, (0, 2)) == 5

def test_get_data():
    assert get_trail_map("data_middle_test.txt") == middle_t_map

def test_main():
    assert main("data_middle_test.txt") == 36