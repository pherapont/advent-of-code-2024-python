from hiking_trails import get_trail_score
import data_simple_test

def test_get_simple_trail_score():
    assert get_trail_score(data_simple_test.t_map, (0, 3)) == 2