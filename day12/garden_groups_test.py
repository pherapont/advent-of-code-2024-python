import pytest
from garden_groups import garden_regions

def test_simple_garden():
    data = [["A", "A", "A", "A"], 
            ["B", "B", "C", "D"], 
            ["B", "B", "C", "C"], 
            ["E", "E", "E", "C"]] 
    assert garden_regions(data) == 140
