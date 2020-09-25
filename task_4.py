class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Поехала!')

    def stop(self):
        print(f'Остановилась!')

    def turn(self, direction):
        print(f'Повернула на {direction}')

    def show_speed(self):
        print(f'Значение скорости')


class TownCar(Car):
