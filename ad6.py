import csv
from datetime import datetime

def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


def compensation(csv):
    for i in csv:
        given_date = datetime.strptime(i["Date of employment"], "%Y-%m-%d")
        current_date = datetime.now()
        year_diff = current_date.year - given_date.year

        if (current_date.month, current_date.date)<(given_date.month, given_date.date):
            year_diff-=1

        if year_diff>=5:
            print(f"name: {i['Name']} - compensation: {year_diff*1000}")



file_path = '6_input.csv'
csv_data = read_csv(file_path)
compensation(csv_data)

