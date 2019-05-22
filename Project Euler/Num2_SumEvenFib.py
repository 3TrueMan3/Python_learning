fib = [0, 1]
summ = 0
for i in range(2, 34):
    tmp = fib[i-2] + fib[i-1]
    if tmp <= 4000000:
        fib.append(tmp)
    else:
        break
for i in fib:
    if i % 2 == 0:
        summ += i
print(summ)