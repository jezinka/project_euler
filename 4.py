__author__ = 'jezinka'


def ex4(limit):
    return max([i * j for j in range(limit//10, limit) for i in range(limit//10, limit) if str(i * j) == str(i * j)[::-1]])


assert ex4(100) == 9009

print(ex4(1000))
