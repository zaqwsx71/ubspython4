import pytest
from ad5 import read_csv

def test_read_csv():
    file_path = 'test_input.csv'
    expected_data = [
        {'Name': 'Adam', 'Salary': '10000', 'Duration of employment in years': '4'},
        {'Name': 'Beata', 'Salary': '12000', 'Duration of employment in years': '5'}
    ]
    actual_data = read_csv(file_path)
    assert actual_data == expected_data

def test_compensation_calculation():
    employee_data = {'Name': 'Beata', 'Salary': '12000', 'Duration of employment in years': '5'}
    expected_compensation = 5000
    actual_compensation = int(employee_data['Duration of employment in years']) * 1000
    assert actual_compensation == expected_compensation

if __name__ == '__main__':
    pytest.main()
