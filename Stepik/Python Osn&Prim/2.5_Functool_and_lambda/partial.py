from functools import partial

x = int("1101", base=2)
print(x)
int_2 = partial(int, base=2)
x = int_2("11011")
print(x)