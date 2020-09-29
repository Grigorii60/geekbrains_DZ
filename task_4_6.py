class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула на {direction}.')

    def show_speed(self):
        print(f'У {self.name} значение скорости {self.speed}.')


class TownCar(Car):
    def show_speed(self):
        print(
            f'{self.name} движущийся со скоростью {self.speed} превышает скорость.' \
                if self.speed > 60 else f'{self.name} движущийся со скоростью {self.speed}.')


class WorkCar(Car):
    def show_speed(self):
        print(
            f'{self.name} движущийся со скоростью {self.speed} превышает скорость.' \
                if self.speed > 40 else f'{self.name} движущийся со скоростью {self.speed}.')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


police_car = PoliceCar(100, "синяя", "Ментовозка")
police_car.go()
police_car.show_speed()
police_car.turn("лево")
police_car.turn("право")
police_car.stop()

town_car = TownCar(65, "желтая", "Доработка")
town_car.go()
town_car.show_speed()
town_car.turn("лево")
town_car.turn("право")
town_car.stop()

work_car = WorkCar(50, "коричневая", "Лошадка")
work_car.go()
work_car.show_speed()
work_car.turn("лево")
work_car.turn("право")
work_car.stop()

work_car = SportCar(150, "красная", "Ламба")
work_car.go()
work_car.show_speed()
work_car.turn("лево")
work_car.turn("право")
work_car.stop()
