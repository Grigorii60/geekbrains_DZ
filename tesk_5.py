proceeds = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

if proceeds > costs:
    print('Фирма работет в прибыль.')

    profitability = (proceeds - costs) / proceeds
    print(f'Рентабельность выручки: {profitability:.2f}')

    staff = int(input('Введите численность сотрудников: '))
    profit_1 = (proceeds - costs) / staff
    print(f'Прибыль фирмы в рассчете на одного сотрудника: ,{profit_1:.2f}')
elif costs > proceeds:
    print('Фирма работает в убыток.')
else:
    print('Фирма работает в 0.')
