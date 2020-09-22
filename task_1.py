in_file = open("new_file.txt", "w", encoding="utf=8")
while True:
    stroka = input("Введите новую строку, пустая строка выход: ")
    if stroka == "":
        break
    else:
        in_file.write(stroka + "\n")
#       in_file.write('\n')
in_file.close()
# in_file = open("new_file.txt", "r")
# content = in_file.readlines()
# print(content)
