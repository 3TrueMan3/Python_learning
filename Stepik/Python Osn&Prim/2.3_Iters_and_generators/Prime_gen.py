import math
import itertools


def primes():
    i = 2
    while i:
        if not any(i % n == 0 for n in range(2, int(math.sqrt(i)) + 1)):
            yield i
        i += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
