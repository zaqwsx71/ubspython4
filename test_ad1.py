import pytest
from ad1 import *



def test_top_numbers_with_less_than_3_values():
    assert top_numbers([1000, 2000]) is None

def test_top_numbers_with_3_values():
    assert top_numbers([1000, 2000, 1500]) == [2000, 1500, 1000]

def test_top_numbers_with_more_than_3_values():
    assert top_numbers([1000, 2000, 1500, 2500, 1800]) == [2500, 2000, 1800]

def test_top_numbers_with_equal_values():
    assert top_numbers([1000, 1000, 1000, 2000, 2000, 1500]) == [2000, 2000, 1500]

def test_top_numbers_with_negative_values():
    assert top_numbers([-1000, -2000, -1500, -2500, -1800]) == [-1000, -1500, -1800]

if __name__ == "__main__":
    pytest.main()