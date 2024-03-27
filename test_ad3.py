from ad3 import *

def test_department_workforce():
    department_worforce('Management') == "In department: Management working now 4 persons: ['Adam', 'Beata', 'Piotr', 'Agata']"
    department_worforce('Cashier') == "In department: Cashier working now 2 people: ['Mateusz', 'Marian']"
    department_worforce('Kitchen') == "In department: Kitchen working now 2 people: ['Jarek', 'Ania']"

def test_department_workforce_with_empty_list():
    department_worforce('') == "List is empty"