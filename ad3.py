from typing import List, Dict, Any

employees: List[Dict[str, Any]] = [

{'Id': 1, 'Name': 'Adam', 'Department': 'Management', 'Salary': 10000},

{'Id': 2, 'Name': 'Beata', 'Department': 'Management', 'Salary': 12000},

{'Id': 3, 'Name': 'Jarek', 'Department': 'Kitchen', 'Salary': 7000},

{'Id': 4, 'Name': 'Agnieszka', 'Department': 'House Floor', 'Salary': 8500},

{'Id': 5, 'Name': 'Marek', 'Department': 'House Floor', 'Salary': 11200},

{'Id': 6, 'Name': 'Ania', 'Department': 'Kitchen', 'Salary': 9300},

{'Id': 7, 'Name': 'Piotr', 'Department': 'Management', 'Salary': 15100},

{'Id': 8, 'Name': 'Mateusz', 'Department': 'Cashier', 'Salary': 18000},

{'Id': 9, 'Name': 'Agata', 'Department': 'Management', 'Salary': 16400},

{'Id': 10, 'Name': 'Marian', 'Department': 'Cashier', 'Salary': 11000},

]

def department_worforce(department):
    try:
        if len(employees) == 0:
            raise ValueError("List is empty")

        lista = []
        for employee in employees:
            if employee['Department'] == department:
                lista.append(employee['Name'])

        return f"In department: {department} working now {len(lista)} people: {lista}"

    except ValueError as e:
        return str(e)

print(department_worforce('Kitchen'))