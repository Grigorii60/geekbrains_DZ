def my_func(x, y):

    """Первый способ"""
    print(x ** y)

    """Второй способ"""
    my_list = (list(str(x) * abs(y)))
    print(my_list)
    mult = 1
    for i in my_list:
        mult = int(i) * mult
    print(1 / mult)


my_func(5, -3)
