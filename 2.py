__author__ = 'jezinka'

fib = [1, 1]

while(fib[-2] + fib[-1] < 4000000):
    fib.append(fib[-2] + fib[-1])

print sum([f for f in fib if f % 2 == 1])

