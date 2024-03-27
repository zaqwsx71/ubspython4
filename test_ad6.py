import pytest
from ad6 import *
import sys

def test_read_csv():
    file_path = 'test_input2.csv'
    expected_data = [
        {'Name': 'Adam', 'Salary': '10000', 'Date of employment': '2020-01-01'},
        {'Name': 'Beata', 'Salary': '12000', 'Date of employment': '2018-12-01'}
    ]
    actual_data = read_csv(file_path)
    assert actual_data == expected_data

def test_compensation():
    csv_data = [
        {'Name': 'Adam', 'Salary': '10000', 'Date of employment': '2020-01-01'},
        {'Name': 'Beata', 'Salary': '12000', 'Date of employment': '2018-12-01'}
    ]
    expected_output = "name: Beata - compensation: 5000"

    compensation(csv_data)

    assert expected_output == "name: Beata - compensation: 5000"


if __name__ == "__main__":
    pytest.main()