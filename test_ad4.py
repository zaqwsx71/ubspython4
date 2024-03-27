import pytest
from ad4 import *


def test_empty_list():
    assert id_with_first_letter([]) == []


def test_missing_id_key():
    employees = [{'Name': 'Adam', 'Department': 'Management', 'Salary': 10000}]
    with pytest.raises(KeyError):
        id_with_first_letter(employees)

# Test dla brakującego klucza 'Name'
def test_missing_name_key():
    employees = [{'Id': 1, 'Department': 'Management', 'Salary': 10000}]
    with pytest.raises(KeyError):
        id_with_first_letter(employees)

def test_id_with_first_letter():
    result = id_with_first_letter(employees)
    assert len(result) == len(employees) # Sprawdzenie czy liczba elementów w zwróconej liście jest taka sama jak w oryginalnej liście

    for i, employee in enumerate(employees):
        key = str(employee['Id'])
        value = str(employee['Name'][0])
        assert {key: value} in result # Sprawdzenie czy para klucz-wartość znajduje się w zwróconej liście


if __name__ == "__main__":
    pytest.main()