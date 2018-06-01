def ex6(number):
    array = range(1, number + 1)
    return square_sum(array) - sum_square(array)


def square_sum(array):
    return sum(array) ** 2


def sum_square(array):
    return sum([x ** 2 for x in array])


assert square_sum([1, 2, 3]) == 36
assert sum_square([1, 2, 3]) == 14
assert sum_square(range(1, 11)) == 385

assert ex6(10) == 2640

print(ex6(100))
