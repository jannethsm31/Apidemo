import csv
import json


def csv_to_json(input_csv_file, json_file):
    with open(input_csv_file, mode= 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]


    with open(output_json_file, 'w') as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    input_csv_file = 'contactos.csv'
    output_json_file = 'contactos.json'
    csv_to_json(input_csv_file, output_json_file)


