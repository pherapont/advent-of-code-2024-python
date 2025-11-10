import pytest
from claw_machines import (
    get_cheapest_way,
    get_result_steps,
    )

def test_one_prize():
    a = (94, 34)
    b = (22, 67)
    location = (8400, 5400)
    assert get_cheapest_way(a, b, location) == 280

def test_simple_result_steps():
    a = 2
    b = 3
    location = 10
    assert get_result_steps(a, b, location) == {(5, 0), (2, 2)}