reit = [7, 5, 3, 3, 2]
while True:
    el_unit_q = input('Введите число или end: ')
    if el_unit_q == 'end':
        break
    else:
        el_unit = int(el_unit_q)

        for el in reit:
            if el_unit > el:
                position_el = reit.index(el)
                print(position_el)
                reit.insert(position_el, el_unit)
                print(reit)
                break