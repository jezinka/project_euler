def nwd(a, b):
    if b is 0:
        return a
    else:
        return nwd(b, a % b)


def nww(array):
    if len(array) == 2:
        a = array[0]
        b = array[1]
        return a // nwd(a, b) * b
    else:
        return nww([array[0], nww(array[1:])])


def ex5(number):
    return nww(range(2, number))


assert nwd(6, 9) == 3
assert nwd(9, 120) == 3

assert nww([6, 9]) == 18
assert nww([5, 6, 12]) == 60

assert ex5(10) == 2520

print(ex5(20))
