def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < 3:
        return signature[:n]
    i = 3
    while i < n:
        signature.append((signature[i-1] + signature[i-2] + signature[i-3]))
        i += 1
    return signature


print(tribonacci([1,1,1], 10))

