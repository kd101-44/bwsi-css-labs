import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_different_order():
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_two_sum_negative_numbers():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_two_sum_large_numbers():
    assert two_sum([1000000, 500000, 1500000], 2000000) == [0, 2]

def test_two_sum_adjacent():
    assert two_sum([1, 3, 2, 4], 5) == [1, 3]