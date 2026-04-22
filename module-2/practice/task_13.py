list = [234, 555, 38, 45, -678, 0, 90, -845, 125, -34]

even_list = []
for num in list:
    if num % 2 == 0:
        even_list.append(num)

even_odd = []
for num in list:
    if num % 2 != 0:
        even_odd.append(num)

negative_list = []
for num in list:
    if num < 0:
        negative_list.append(num)

positive_list = []
for num in list:
    if num > 0:
        positive_list.append(num)

print(f"Четные числа: {even_list}")
print(f"Нечетные числа: {even_odd}")
print(f"Отрицательные числа: {negative_list}")
print(f"Положительные числа: {positive_list}")
