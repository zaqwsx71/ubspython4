name_to_salary_dictionary = {

    'Adam': 10000,

    'Beata': 12000,

    'Jarek': 7000,

    'Agnieszka': 8500,

    'Marek': 11200,

    'Ania': 9300,

    'Piotr': 15100,

    'Mateusz': 18000,

    'Agata': 16400,

    'Marian': 11000

}


def mean_from_dict(dict):
    try:
        if len(dict) == 0:
            raise ValueError("Dictionary is empty")

        mean = sum(dict.values()) / len(dict)
        return mean

    except ValueError as e:
        print(f"Error: {e}")
        return None

def salaries_above_average(dict, avg):
    dict2 = {}
    for key, value in dict.items():
        if value > avg:
            dict2[key] = value
    return dict2


avg = mean_from_dict(name_to_salary_dictionary)
if avg is not None:
    high_salaries = salaries_above_average(name_to_salary_dictionary, avg)

    print(f"Salaries greater than mean salary: {avg}\n")
    for key, value in high_salaries.items():
        print(f"name: {key} - salary: {value}")