import sys
from tabulate import tabulate
import csv


def transform_csv_to_tabulate_format(file_path: str):
    try:
        with open(file_path) as file:
            reader = csv.reader(file, delimiter=",")
            data = []
            for row1, row2, row3 in reader:
                dict_data = {'row1': row1, 'row2': row2, 'row3': row3}
                data.append(dict_data)

            return tabulate(data, headers='firstrow', tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    file_path = sys.argv[1]
    print(transform_csv_to_tabulate_format(file_path))
