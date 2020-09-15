product = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    name = input('Наберите end для выхода или нажмите Enter: ')
    if name == 'end':
        break
    num += 1
    for f in features.keys():
        property = input(f'Введите значение свойства "{f}": ')
        features[f] = int(property) if (f == 'цена' or f == 'количество') else property
        analytics[f].append(features[f])
    product.append((num, features))
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30} : {value}')
    print("*" * 30)
