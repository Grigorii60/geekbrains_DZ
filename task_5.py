def my_func(frag):
    new_list = []
    for i in frag:
        try:
            new_list.append(int(i))
        except ValueError:
            print('\n Необходимо вводить цифры.!!!\n')
    return sum(new_list)


full_sum = 0

while True:
    frag = input('Введите числа через пробел, для выхода в конце end: ').split(' ')
    #    print(frag)

    while frag.count('') != 0:
        frag.remove('')
    print(frag)

    if frag[-1] == 'end':
        frag.pop(-1)
        summa = my_func(frag)
        print(f'Сумма новых чисел: {summa}')
        full_sum = full_sum + summa
        print(f'Общая сумма: {full_sum}')
        break
    else:
        summa = my_func(frag)
        print(f'Сумма новых чисел: {summa}')
        full_sum = full_sum + summa
        print(f'Общая сумма: {full_sum}')
