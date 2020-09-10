my_list = (input('Введите слова через пробел: ')).split()
print(my_list)

for el in enumerate(my_list):
    if len(el) < 10:
        print(el)
    else:
        print(el[0:10])

# но так мне нравится больше:
n = 1
for el in my_list:
    if len(el) < 10:
        print(f'{n}. {el}')
        n = n + 1
    else:
        print(f'{n}. {el[0:10]}')
        n = n + 1

