number = int(input('Введите целое, положительное число: '))
max_number = number % 10
while number > 0:
    number = number // 10
    max_number_1 = number % 10
    if max_number_1 > max_number:
        max_number = max_number_1

print(f'Самая большая цифра: {max_number}')
