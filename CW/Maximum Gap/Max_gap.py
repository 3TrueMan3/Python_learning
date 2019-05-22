def max_gap(numbers):
    sort = sorted(numbers)
    return max(sort[i] - sort[i-1] for i in range(1, len(sort)))

print(max_gap([13,10,2,9,5]))