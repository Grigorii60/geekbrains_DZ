from googletrans import Translator

f = open('text_4.txt', 'r')
contents = f.read()
print(contents)
translator = Translator()
result = translator.translate(contents, dest='ru')
print(result.text)
f.close()

"""Основное решение"""

file = open('text_4.txt', 'r', encoding="utf=8")
new_file = open('text_4_1.txt', 'w', encoding="utf=8")
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
for i in file:
    my_list = i.split()
    my_list.insert(0, (my_dict.get(my_list[0])))
    my_list.pop(1)
    n = ' '.join(my_list)
    new_file.write(n + '\n')
file.close()
new_file.close()
