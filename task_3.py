my_f = open('text_3.txt', "r", encoding="utf=8")
unit = 0
summ_zp = 0
result_list = []
for i in my_f:
    unit += 1
    full_str = i.split()
    if float(full_str[1]) > 20000:
        result_list.append(full_str[0])
    summ_zp = summ_zp + float(full_str[1])
print(f'Средняя ЗП {(summ_zp / unit):2}')
print(f"Сотрудники с ЗП больше 20000: {', '.join(result_list)}")
