def find_the_length_using_a_loop(test_list: list):
    number = 0
    for _ in test_list:
        number += 1
    return number


tst = [1, 2, 3, 4]

print(find_the_length_using_a_loop(tst))

new_list = []
for i in tst:
    new_list.append(i)

print(new_list)
