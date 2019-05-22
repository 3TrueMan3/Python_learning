import math
def productFib(prod):
    phi = (1 + math.sqrt(5))/2
    n = math.ceil(math.log(math.sqrt(5)*prod, phi))
    fib = [0,1]
    for i in range(2, n):
        tmp = fib[i-2] + fib[i-1]
        fib.append(tmp)
    for i in range(len(fib)):
        mult = fib[i] * fib[i + 1]
        if mult < prod:
            continue
        elif mult > prod:
            return [fib[i], fib[i + 1], False]
        else:
            return [fib[i], fib[i + 1], True]

print(productFib(585648643216558465123168432958362135468958432135498764251321654984654654894651321654984651321654988496843621354698965132156986513215695))