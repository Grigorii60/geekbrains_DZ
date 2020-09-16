from functools import reduce


def my_func(a, b):
    return a * b


print(reduce(my_func, [el for el in range(100, 1001)]))
