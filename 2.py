__author__ = 'jezinka'


def ex2(fib_array, limit):
    while fib_array[-2] + fib_array[-1] < limit:
        fib_array.append(fib_array[-2] + fib_array[-1])

    return sum([f for f in fib_array if f % 2 == 0])

assert ex2([1, 1], 100) == sum([2, 8, 34])

print ex2([1,1], 4000000)