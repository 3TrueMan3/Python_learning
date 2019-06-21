# x = input().split()
# xs = (int(i) for i in x)
#
#
# evens = list(filter(lambda x: x % 2 == 0, xs))
# print(evens)

x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

import operator as op
from functools import partial

sort_by_last = partial(list.sort, key=op.itemgetter(-1))

print(x)
sort_by_last(x)



# def length(name):
#     return len(' '.join(name))
#
#
# name_lengths = [length(name) for name in x]
# print(name_lengths)
#
# x.sort(key=length)
print(x)
