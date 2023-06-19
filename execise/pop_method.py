def pop_swap(my_list: list):
    """
    Swap the first and last elements is to use the inbuilt function list.pop().
     Pop the first element and store it in a variable.
      Similarly, pop the last element and store it in another variable.
     Now insert the two popped element at each other’s original position.
    :param my_list:
    :return my_list:
    """
    first = my_list.pop(0)
    last = my_list.pop(-1)

    my_list.insert(0, last)
    my_list.append(first)
    return my_list


list1 = [1, 2, 3, 4, 5]
print(pop_swap(list1))
