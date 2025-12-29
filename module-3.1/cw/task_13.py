list = [234, 555, 38, 45, -678, 0, 90, -845, 125, -34]

even_list = []
for num in list:
    if num % 2 == 0:
        even_list.append(num)

even_odd = []
for num in list:
    if num % 2 != 0:
        even_odd.append(num)

