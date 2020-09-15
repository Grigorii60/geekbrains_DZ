def data(name, surname, year, town, email, phone_number):
    print(
        f'{name} {surname}, {year} года рождения, проживающий(ая) в {town}, email - {email}, телефонный номер {phone_number}.')


a = input('Введите имя: ')
b = input('Введите фамилию: ')
c = input('Введите год рождения: ')
d = input('Введите город проживания: ')
e = input('Введите свой email: ')
f = input('Введите свой номер телефона: ')

data(name=a, year=c, surname=b, email=e, phone_number=f, town=d)
