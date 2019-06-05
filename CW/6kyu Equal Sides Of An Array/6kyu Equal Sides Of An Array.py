# Script is about finding array index that sum of members before and after this index are equal

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
