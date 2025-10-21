import pytest
from strange_stones import transform_stones

def test_transform_simple_stones():
    init_stones = ("0", "1", "10", "99", "999")
    transformed = ["1", "2024", "1", "0", "9", "9", "2021976"]
    assert transform_stones(init_stones, 1) == transformed