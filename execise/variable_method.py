def swap(my_list: list):
    """
      # Storing the first and last element
        # as a pair in a tuple variable named any_variable
    """
    any_variable = my_list[-1], my_list[0]
    my_list[0], my_list[-1] = any_variable
    return my_list


if __name__ == "__main__":
    my_lis = [1, 2, 3, 4, 5]
    print(swap(my_lis))
    print(swap.__doc__)
