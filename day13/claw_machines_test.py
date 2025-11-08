import pytest
from claw_machines import get_cheapest_way

def test_one_prize():
    a = (94, 34)
    b = (22, 67)
    location = (8400, 5400)
    assert get_cheapest_way(a, b, location) == 280
