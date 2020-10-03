class MySklad:
    def giv(self):
        product = []
        dict_printer = {'название': '', 'год выпуска': '', 'цвет корпуса': '', 'цвет печати': ''}
        dict_scaner = {'название': '', 'год выпуска': '', 'цвет корпуса': '', 'цветное сканирование': ''}
        dict_xerox = {'название': '', 'год выпуска': '', 'цвет корпуса': '', 'колличество копий': ''}
        analytics_printer = {'название': [], 'год выпуска': [], 'цвет корпуса': [], 'цвет печати': []}
        analytics_scaner = {'название': [], 'год выпуска': [], 'цвет корпуса': [], 'цветное сканирование': []}
        analytics_xerox = {'название': [], 'год выпуска': [], 'цвет корпуса': [], 'колличество копий': []}
        num = 0
        while True:
            name = input(
                'Наберите 0 для выхода, Принтер-1, Сканер-2, Ксерокс-3, 4 для просмотра склада и нажмите Enter: ')

            if name == '0':
                break
            num += 1
            if name == '1':
                for f in dict_printer.keys():
                    property = input(f'Введите значение свойства "{f}": ')
                    dict_printer[f] = int(property) if f == 'год выпуска' else property
                    analytics_printer[f].append(dict_printer[f])
                    print(dict_printer)
                product.append((num, dict_printer))
            elif name == '2':
                for f in dict_scaner.keys():
                    property = input(f'Введите значение свойства "{f}": ')
                    dict_scaner[f] = int(property) if f == 'год выпуска' else property
                    analytics_scaner[f].append(dict_scaner[f])
                product.append((num, dict_scaner))
            elif name == '3':
                for f in dict_xerox.keys():
                    property = input(f'Введите значение свойства "{f}": ')
                    dict_xerox[f] = int(property) if f == 'год выпуска' else property
                    analytics_xerox[f].append(dict_xerox[f])
                product.append((num, dict_printer))
            elif name == '4':
                name = input(
                    'Наберите Принтер-1, Сканер-2, Ксерокс-3, 4 для просмотра склада и нажмите Enter: ')
                if name == '1':
                    print(f'\n Текущая аналитика по принтерам: \n {"*" * 30}')
                    for key, value in analytics_printer.items():
                        print(f'{key[:25]:>30} : {value}')
                    print("*" * 30)
                elif name == '2':
                    print(f'\n Текущая аналитика по сканерам: \n {"*" * 30}')
                    for key, value in analytics_scaner.items():
                        print(f'{key[:25]:>30} : {value}')
                    print("*" * 30)
                elif name == '3':
                    print(f'\n Текущая аналитика по ксероксам: \n {"*" * 30}')
                    for key, value in analytics_xerox.items():
                        print(f'{key[:25]:>30} : {value}')
                    print("*" * 30)
        print(product)


class Orgtehnik:
    def __init__(self, name, year, color_body):
        self.name = name
        self.year = year
        self.color_body = color_body


class Printer(Orgtehnik):
    def __init__(self, name, year, color_body, ptint_color):
        super().__init__(name, year, color_body)
        self.print_color = ptint_color


class Scaner(Orgtehnik):
    def __init__(self, name, year, color_body, scan_color):
        super().__init__(name, year, color_body)
        self.scan_color = scan_color

    def g(self):
        print(self.scan_color)
        print(self.color_body)


class Xerox(Orgtehnik):
    def __init__(self, name, year, color_body, copy):
        super().__init__(name, year, color_body)
        self.copy = copy


a = MySklad()
a.giv()
