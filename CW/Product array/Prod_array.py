import numpy as np


def product_array(numbers):
    answer = []
    return [int(np.product(numbers) / numbers[i]) for i in range(len(numbers))]

print(product_array([3,27,4,2]))
