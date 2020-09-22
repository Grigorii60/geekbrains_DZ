in_file = open("new_file_2.txt", "w", encoding="utf=8")
record = in_file.write('1 2 3 4 5 6 7 8 9')
in_file.close()

in_file =open('new_file_2.txt', 'r', encoding="utf=8")
my_list = ' '.join(in_file)
print(my_list)
sum = 0
for num in my_list:
    if num != " ":
        sum = sum + int(num)
print(f'Сумма чисел равна: {sum}.')