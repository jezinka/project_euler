__author__ = 'jezinka'

from math import sqrt

def sieve(numbers):
    number_array = [False]*numbers
    number_array[0] = number_array[1] = True
    for i in range(2, int(sqrt(len(number_array)))):
        if number_array[i]:
            continue
        else:
            for j in range(2*i, len(number_array), i):
                number_array[j] = True
    return [i for i, x in enumerate(number_array) if not x]

