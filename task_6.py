from itertools import count, islice, cycle

for el in islice(count(7), 9):
    print(el)

my_list = [el for el in islice(count(7), 9)]
print(my_list)

for el in islice(cycle(my_list), 50):
    print(el)
