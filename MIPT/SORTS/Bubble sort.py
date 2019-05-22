def up_bubble_sort(lst: list):
    for i in range(len(lst)):
        for j in range(1, len(lst)):
            if lst[j] < lst[j-1]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst


def down_bubble_sort(lst: list):
    for i in range(len(lst)):
        for j in range(1, len(lst)):
            if lst[j] > lst[j-1]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst


print('Введите массив через пробел')
a = [int(i) for i in input().split(' ')]

print(up_bubble_sort(a))
print(down_bubble_sort(a))
