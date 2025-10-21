import pytest
from hiking_trails import get_trail_score, get_trail_map, get_trail_raiting, main
from data_simple_test import t_map as simple_t_map
from data_middle_test import t_map as middle_t_map

def test_get_simple_trail_score():
    assert get_trail_score(simple_t_map, (0, 3)) == 2

def test_get_middle_trail_score():
    assert get_trail_score(middle_t_map, (0, 2)) == 5

def test_get_data():
    assert get_trail_map("data_middle_test.txt") == middle_t_map

@pytest.mark.skip(reason="this test for part 1")
def test_main_score():
    assert main("data_middle_test.txt") == 36

def test_get_middle_trail_raiting():
    assert get_trail_raiting(middle_t_map, (0, 2)) == 20

def test_main_rainting():
    assert main("data_middle_test.txt") == 81