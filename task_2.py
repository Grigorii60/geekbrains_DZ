class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass_1=25, thickness=5):
        mass = self._length * self._width * mass_1 * thickness
        print(f'Масса афальта равна: {mass/1000} т.')


asphalt = Road(int(input(f'Введите длину в метрах: ')), int(input(f'Введите ширину в метрах: ')))
asphalt.mass()
