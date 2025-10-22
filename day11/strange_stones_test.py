import pytest
from strange_stones import transform_stones ,get_data_from_file, main

def test_get_data_from_file():
    assert get_data_from_file("test_data.txt") == ("125", "17")

def test_transform_simple_stones():
    init_stones = ("0", "1", "10", "99", "999")
    transformed = ["1", "2024", "1", "0", "9", "9", "2021976"]
    blink_count = 1
    assert transform_stones(init_stones, blink_count) == transformed

def test_transform_middle_stones_1_blink():
    init_stones = ("125", "17") 
    transformed = ["253000", "1", "7"]
    blink_count = 1
    assert transform_stones(init_stones, blink_count) == transformed

def test_transform_middle_stones_2_blink():
    init_stones = ("125", "17") 
    transformed = ["253", "0", "2024", "14168"] 
    blink_count = 2
    assert transform_stones(init_stones, blink_count) == transformed

def test_transform_middle_stones_3_blink():
    init_stones = ("125", "17") 
    transformed = ['512072', '1', '20', '24', '28676032']
    blink_count = 3
    assert transform_stones(init_stones, blink_count) == transformed

def test_transform_middle_stones_4_blink():
    init_stones = ("125", "17") 
    transformed = ['512', '72', '2024', '2', '0', '2', '4', '2867', '6032']
    blink_count = 4
    assert transform_stones(init_stones, blink_count) == transformed

def test_transform_middle_stones_6_blink():
    init_stones = ("125", "17") 
    transformed = ['2097446912', '14168', '4048', '2', '0', '2', '4', '40', '48', '2024', '40',
                    '48', '80', '96', '2', '8', '6', '7', '6', '0', '3', '2']         
    blink_count = 6
    assert transform_stones(init_stones, blink_count) == transformed

def test_main():
    assert main("test_data.txt", 25) == 55312