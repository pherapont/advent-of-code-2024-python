import pytest
from claw_machines import (
    get_cheapest_way,
    get_initial_steps_count,
    get_cheapest_coordinates,
    )

@pytest.mark.skip(reason="while in rest")
def test_initial_steps_count():
    machine = (10, 20)
    location = (101, 55)
    assert get_initial_steps_count(machine, location) == 14

@pytest.mark.skip(reason="while in rest")
def test_one_prize():
    a = (94, 34)
    b = (22, 67)
    location = (8400, 5400)
    assert get_cheapest_way(a, b, location) == 280

def test_simple_cheapest_coordinates():
    a = (2, 2)
    b = (3, 3)
    location = (10, 10)
    assert get_cheapest_coordinates(a, b, location) == (5, 0)