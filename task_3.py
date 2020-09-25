class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'Работник {self.position} {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Его доход: {sum(self._income.values())}')


income = {"wage": 50000, "bonus": 20000}
result = Position('Сергей', 'Иванов', 'менеджер', income)
result.get_full_name()
result.get_total_income()
