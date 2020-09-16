from sys import argv

name, time, time_rate, prize = argv


def zp(time, time_rate, prize):
    zp = int(time) * int(time_rate) + int(prize)
    print(zp)


zp(time, time_rate, prize)
