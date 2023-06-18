def swap_list(list):
    a, *b, c = list
    list = [c, *b, a]
    return list


list1 = [1,2,3,4,5]
print(swap_list(list1))
