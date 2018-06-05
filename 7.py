import math


def ex7(number):
    return sieve(number ** 2)[number]


def sieve(number):
    array = number * [True]
    array[0] = array[1] = False
    for i in range(2, int(math.sqrt(len(array)))):
        if array[i]:
            for j in range(i ** 2, len(array), i):
                array[j] = False
    return [i for i, x in enumerate(array) if x]


print(ex7(5))
assert ex7(5) == 13
print(ex7(10000))
