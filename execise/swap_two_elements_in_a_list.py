import sys


def swap_two_elements_from_a_list(my_list: list, first: int, second: int) -> list:
    """
     Simple swap, using comma assignment
     Since the positions of the elements are known,
      we can simply swap the positions of the elements.
    :param my_list:
    :param first:
    :param second:
    :return my_list:
    """
    my_list[first], my_list[second] = my_list[second], my_list[first]
    return my_list


list1 = [1, 2, 3, 4, 5]

print(swap_two_elements_from_a_list(list1, 1, 2))
print(print.__doc__)
sys.stdout.write("git status")
