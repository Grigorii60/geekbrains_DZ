my_f = open("new_file.txt", "r", encoding="utf=8")
content = my_f.readlines()
print(content)
n = 0
for a in content:
    n += 1
    s = 0
    sl_str = a.split()
    for b in sl_str:
        s += 1
    print(f'Колличество слов в {n} строке - {s}.')
print(f'Колличество строк в new_file.txt - {n}.')
my_f.close()
