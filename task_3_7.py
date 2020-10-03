class Cell:
    def __init__(self, nums):
        self.nums = nums
    def make_order(self,long):
        return '\n'.join(['*' * long for _ in range(self.nums// long)]) + '\n' + '*' * (self.nums % long)
    def __add__(self, other):
        return f'Число ячеек общей клетки равно: {self.nums + other.nums}'
    def __sub__(self, other):
        if self.nums - other.nums > 0:
            return f'Результат вычетания: {self.nums - other.nums}'
        else:
            return f'Разность колличества ячеек меньше нуля!'
    def __mul__(self, other):
        return f'В новой клетке ячеек: {self.nums * other.nums}'
    def __floordiv__(self, other):
        return f'В новой клетке ячеек: {self.nums//other.nums}'

cell_1 = Cell(15)
cell_2 = Cell(13)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1//cell_2)