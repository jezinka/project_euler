__author__ = 'jezinka'


def get_next_prime(factor):
    if factor == 1:
        return 2

    factor += 1

    for n in range(2, factor):
        if factor % n == 0:
            return get_next_prime(factor)

    return factor


def split_ahead(number, i):
    while number % i == 0:
        number /= i
    return number


def ex3(number):

    i = 1

    while number != 1:
        i = get_next_prime(i)
        number = split_ahead(number, i)

    return i

assert get_next_prime(0) == 1
assert get_next_prime(1) == 2
assert get_next_prime(3) == 5
assert get_next_prime(8) == 11

assert ex3(13195) == 29

print ex3(600851475143)

