# Given a list, write a Python program to swap first and last element of the list.
#
# Examples:
#
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
#
# Input : [1, 2, 3]
# Output : [3, 2, 1]


def swap_list(l: list):
    """
    The last element of the list can be referred as list[-1].
    Therefore, we can simply swap list[0] with list[-1]
    """
    l[0], l[-1] = l[-1], l[0]
    print(l)


if __name__ == "__main__":
    our_list = [1, 2, 3, 4, 5]
    swap_list(our_list)
    print(swap_list.__doc__)
