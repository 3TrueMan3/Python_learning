from itertools import product

for roll in product([1, 2, 3, 4, 5, 6], repeat=3):
    x.append(list(roll))
print(x)