def find_nb(m):
    
    for i in range(m//2, 3, -1):
        n = m // i
        
        sum = 0
        for j in range(n):
            sum += (n - j) ** 3
            if sum > m:
                break
        if sum == m:
            return n
    return -1


print(find_nb(4183059834009))
