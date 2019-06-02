def zeros(n):
    x = 0
    while n != 0:
        x += n // 5
        n = n // 5
    return x


print(zeros(6))
