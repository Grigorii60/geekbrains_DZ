import time
from turtle import *

t = Turtle()


class TrafficLight:
    __color = 'цвет'

    def running(self):
        t.screen.setup(300, 300)
        t.screen.bgcolor("red")
        time.sleep(7)
        t.screen.bgcolor("yellow")
        time.sleep(3)
        t.screen.bgcolor("green")
        time.sleep(7)


color_1 = TrafficLight()
color_1.running()
