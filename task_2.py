new_list = []
el = None
while el != 'end':
    el = (input('Введите элемент списка, когда введете все наберите end: '))
    new_list.append(el)
new_list.pop(-1)

print(new_list)

for i in range(len(new_list)):
    if i % 2 == 0:
        new_list.insert(i+2, new_list[i])
        new_list.pop(i)
print(new_list)

