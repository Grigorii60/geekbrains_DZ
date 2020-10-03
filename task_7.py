class Complex:
    def __init__(self, nums):
        self.nums = nums

    def __add__(self, other):
        return f'Сумма комплексных чисел: {self.nums + other.nums}'

    def __mul__(self, other):
        return f'Умножение комплексных чисел: {self.nums * other.nums}'
comp_1 = Complex(complex(1, 2))
comp_2 = Complex(complex(3,4))
print(comp_1 + comp_2)
print(comp_1 * comp_2)