import pytest
from ad2 import *


def test_mean_from_dict():
    assert mean_from_dict(name_to_salary_dictionary) == 11850.0
    assert mean_from_dict({}) is None


def test_salaries_above_average():
    avg = mean_from_dict(name_to_salary_dictionary)
    high_salaries = salaries_above_average(name_to_salary_dictionary, avg)
    assert high_salaries == {'Agata': 16400, 'Beata': 12000, 'Mateusz': 18000, 'Piotr': 15100}

if __name__ == "__main__":
    pytest.main()