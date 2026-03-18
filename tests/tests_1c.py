<<<<<<< Updated upstream
import pytest
from labs.lab_1.lab_1c import max_subarray_sum
=======
<<<<<<< HEAD
# tests/tests_1c.py

import pytest
from labs.lab_1.lab_1c import max_subarray_sum  # <- correct path
=======
import pytest
from labs.lab_1.lab_1c import max_subarray_sum
>>>>>>> 6582b4869d920d8afb1e54e1e7340c28e1f2fca7
>>>>>>> Stashed changes

def test_mixed_numbers():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_all_positive():
    assert max_subarray_sum([1,2,3,4]) == 10

def test_all_negative():
    assert max_subarray_sum([-1,-2,-3,-4]) == -1

def test_single_element():
    assert max_subarray_sum([5]) == 5

def test_zeroes():
    assert max_subarray_sum([0,0,0]) == 0

def test_large_negative_prefix():
    assert max_subarray_sum([-100,1,2,3]) == 6

def test_empty_list():
    with pytest.raises(ValueError):
        max_subarray_sum([])