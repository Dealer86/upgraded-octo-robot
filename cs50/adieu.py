
def bid_adieu(names):
    num_names = len(names)
    if num_names == 1:
        return f"Adieu, adieu, to {names[0]}"
    else:
        last_name = names[-1]
        names = names[:-1]
        joined_names = ', '.join(names)
        if num_names == 2:
            return f"Adieu, adieu, to {joined_names} and {last_name}"
        else:
            return f"Adieu, adieu, to {joined_names}, and {last_name}"


def main():
    names = []
    print("Enter names (Ctrl+D to finish):")
    while True:
        try:
            name = input()
            names.append(name)
        except EOFError:
            break

    farewell = bid_adieu(names)
    print(farewell)


if __name__ == "__main__":
    main()






