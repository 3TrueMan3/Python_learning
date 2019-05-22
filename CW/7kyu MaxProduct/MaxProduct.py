def adjacent_element_product(array: list):

    return max(array[i] * array[i-1] for i in range(1, len(array)))


print(adjacent_element_product([]))
