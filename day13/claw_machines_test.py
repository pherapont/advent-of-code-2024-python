import pytest
from claw_machines import (
    get_cheapest_way,
    get_result_steps,
    )

def test_simple_result_steps():
    a = 2
    b = 3
    location = 10
    assert get_result_steps(a, b, location) == {(5, 0), (2, 2)}

def test_1_prize():
    a = (94, 34)
    b = (22, 67)
    location = (8400, 5400)
    assert get_cheapest_way(a, b, location) == 280

def test_2_prize():
    a = (17, 86)
    b = (84, 37)
    location = (7870, 6450)
    assert get_cheapest_way(a, b, location) == 200

def test_1_empty():
    a = (69, 23)
    b = (27, 71)
    location = (18641, 10279)
    assert get_cheapest_way(a, b, location) == 0

def test_2_empty():
    a = (26, 66)
    b = (67, 21)
    location = (12748, 12176)
    assert get_cheapest_way(a, b, location) == 0