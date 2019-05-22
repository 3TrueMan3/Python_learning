def order(sentence):
    lst = [s for s in sentence.split(' ')]
    for i in range(1, len(lst)):
        if lst[i-1].find(str(i)) == True:
            continue
        else:
            lst[i-1], lst[i] = lst[i], lst[i-1]
    return lst


print(order("is2 Thi1s T4est 3a"))
