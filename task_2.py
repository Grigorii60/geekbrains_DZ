time_sec = int(input('Введите число в секундах: '))

hour = int(time_sec / 3600)
minute = int((time_sec - (hour * 3600)) / 60)
second = time_sec - ((hour * 3600) + (minute * 60))

print(f'{time_sec} секунд это {hour}:{minute}:{second} в формате чч:мм:сс')

# второй вариант наверное более правильный

time_sec = int(input('Введите число в секундах: '))

hour = int(time_sec / 3600)
minute = int((time_sec % 3600) / 60)
second = time_sec % 60

print(f'{time_sec} секунд это {hour}:{minute}:{second} в формате чч:мм:сс')
