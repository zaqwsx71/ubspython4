salaries = [10000, 12000, 7000, 8500, 11200, 9300, 15100, 18000, 16400, 11000]


def top_numbers(salaries_list):
    try:
        if len(salaries_list) < 3:
            raise ValueError("List must contain at least 3 amounts")

        sorted_sal = sorted(salaries_list, reverse=True)
        top_sal = sorted_sal[:3]
        return top_sal

    except ValueError as e:
        print(f"Error: {e}")
    return None