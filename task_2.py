class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt
nam_1 = input('Введите первое число: ')
nam_2 = input('Введите второе число: ')

try:
    if int(nam_2) == 0:
        raise MyError('Нельзя делить на нуль.')
    division = int(nam_1) / int(nam_2)
except ValueError:
    print('Вы ввели не число!')
except MyError as err:
    print(err)
else:
    print(f'Результат деления: {division}')