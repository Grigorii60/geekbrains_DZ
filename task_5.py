class Stationery:
    title = 'SKR'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки Pen')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки Pencil')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки Handle')


a = Stationery()
a.draw()
b = Pen()
b.draw()
c = Pencil()
c.draw()
d = Handle()
d.draw()
