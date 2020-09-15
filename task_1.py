def division(number_1, number_2):
    """ Сделлаем функцию деления и отработаем ошибки"""
    try:
        result = int(number_1) / int(number_2)
        print(f'Результат деления: {result}')
    except ValueError:
        print('Нужны два числа')
    except ZeroDivisionError:
        print('На ноль делить нельзя')


number_1 = input('Введите первое число и нажмите Enter: ')
number_2 = input('Введите второе число и нажмите Enter: ')

division(number_1, number_2)
