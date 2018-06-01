__author__ = 'jezinka'


def ex1(limit):
    return sum([i for i in range(1, limit) if i % 3 == 0 or i % 5 == 0])


assert ex1(10) == 23

print(ex1(1000))
