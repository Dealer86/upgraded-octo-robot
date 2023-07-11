import sys


def count_lines_of_code(file_path: str):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    count = 0
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            count += 1

    return count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]
    lines_of_code = count_lines_of_code(file_path)
    print(lines_of_code)
