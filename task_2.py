from random import randint

list = []
i = 0
while i < 15:
    list.append(randint(0, 1000))
    i += 1
print(list)
# list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in list if el > list[list.index(el) - 1]]
if list[0] > list[-1]:
    new_list.pop(0)
print(new_list)
