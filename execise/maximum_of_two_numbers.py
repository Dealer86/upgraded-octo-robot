def maximum_of_two_numbers(first: int, second: int):
    if first > second:
        return first
    else:
        return second


print(maximum_of_two_numbers(1, 10))

print(max(1, 10))


def second_method(a, b):
    return a if a >= b else b


print(second_method(1, 10))

maximul = lambda a, b: a if a >= b else b

print(maximul(1, 10))


def min_of_two_number(a, b) -> int:
    return a if a < b else b


print(min_of_two_number(1, 10))

min_of_two_numbers = lambda a, b: a if a <= b else b

print(min_of_two_numbers(10, 100))
