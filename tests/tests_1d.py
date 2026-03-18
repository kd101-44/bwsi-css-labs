import pytest
from labs.lab_1.lab_1d import two_sum

def check_two_sum_result(nums, target, result):
    assert len(result) == 2
    i, j = result
    assert i != j
    assert nums[i] + nums[j] == target

def test_two_sum_basic():
    check_two_sum_result([2, 7, 11, 15], 9, two_sum([2, 7, 11, 15], 9))

def test_two_sum_different_order():
    check_two_sum_result([3, 2, 4], 6, two_sum([3, 2, 4], 6))

def test_two_sum_negative_numbers():
    check_two_sum_result([-1, -2, -3, -4, -5], -8, two_sum([-1, -2, -3, -4, -5], -8))

def test_two_sum_large_numbers():
    check_two_sum_result([1000000, 500000, 1500000], 2000000, two_sum([1000000, 500000, 1500000], 2000000))

def test_two_sum_adjacent():
    check_two_sum_result([1, 3, 2, 4], 5, two_sum([1, 3, 2, 4], 5))