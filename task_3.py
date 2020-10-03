class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


nam_1 = 0
my_list = []
while nam_1 != 'stop':
    try:
        nam_1 = input('Введите элемент, для завершения stop: ')
        if nam_1.isdigit() == False:
            raise MyError('Вводим только числа.')
    except MyError as err:
        print(err)
    else:
        my_list.append(nam_1)
print(f'Наш список: {my_list}')