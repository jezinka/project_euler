__author__ = 'jezinka'


def get_next_prime(factor):
    if factor == 1:
        return 2

    factor += 1

    for n in range(2, factor):
        if factor % n == 0:
            return get_next_prime(factor)

    return factor


def ex3():
    number = 600851475143
    i = 1

    while number != 1:
        i = get_next_prime(i)
        while number % i == 0:
            number /= i

    return i

print ex3()

