import pytest
from claw_machines import (
    get_cheapest_way,
    get_initial_steps_count,
    )

def test_initial_steps_count():
    machine = (10, 20)
    location = (101, 55)
    assert get_initial_steps_count(machine, location) == 14

def test_one_prize():
    a = (94, 34)
    b = (22, 67)
    location = (8400, 5400)
    assert get_cheapest_way(a, b, location) == 280
