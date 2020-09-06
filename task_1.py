name = input('Как твое имя? : ')
print(f'Привет {name}, а мое Григорий.')

age = int(input('А сколько тебе лет? : '))
my_age = 36

if age == my_age:
    print('Мы ровестники!')
elif age > my_age:
    print(f'{name} ты старше меня на {age - my_age} лет.')
else:
    print(f'{name} ты младше меня на {my_age - age} лет.')

result = input('Надеюсь я понял задание и сделал все верно? : ')
if result == ["Да", "да", "Yes", "yes"]:
    print(f'{name} отлично, тогда я перехожу к следующему!')
else:
    print(f'{name} жаль, но я обещаю стараться!)))')
