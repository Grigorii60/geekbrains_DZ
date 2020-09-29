from abc import ABC, abstractmethod


class Clothers:
    @abstractmethod
    def my_clothers(self):
        print('Посчитаем расход ткани:')


class Coat(Clothers):
    def __init__(self, v):
        self.v = v

    def use_tk(self):
        return round((self.v / 6.5 + 0.5), 2)


class Suit(Clothers):
    def __init__(self, h):
        self.h = h

    def use_suit(self):
        return round((2 * self.h + 0.3), 2)

    @property
    def finish(self):
        return ('Расчет окончен!')


clow = Clothers()
clow.my_clothers()
clow_1 = Coat(38)
clow_2 = Suit(1.8)
print(clow_1.use_tk())
print(clow_2.use_suit())
print(clow_2.finish)
