import csv

def read_csv(file_path):
    data = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    return data

def compensation_calculation(csv):
    for i in csv:
        if int(i["Duration of employment in years"])>=5:
            print(f"name: {i['Name']} - compensation: {int(i['Duration of employment in years'])*1000}")


file_path = '5_input.csv'
csv_data = read_csv(file_path)
compensation_calculation(csv_data)