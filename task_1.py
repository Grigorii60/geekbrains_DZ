class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date):
        day, month, year = map(int, date.split('-'))
        return cls(day, month, year)

    @staticmethod
    def is_date_valid(date):
        day, month, year = map(int, date.split('-'))
        if day <= 31 and month <= 12 and year <= 2099:
            print(day, month, year)
        else:
            print('Дата введена некорректно.')
Date.from_string('11-09-2100')
Date.is_date_valid('11-09-2100')

