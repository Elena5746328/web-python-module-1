list = [-5, 6, 9, 0, -3, 35, 44, 23, 90, -65]

sum_negative = sum(x for x in list if x < 0)

sum_even = sum(x for x in list if x % 2 == 0)

sum_odd = sum(x for x in list if x % 2 != 0)

product_index3 = 1
for i in range(0, len(list), 3):
    product_index3 *= list[i]

min_val = min(list)
max_val = max(list)
min_index = list.index(min_val)
max_index = list.index(max_val)
left_index = min(min_index, max_index)
rigth_index = max(min_index, max_index)
elements_between = list[left_index + 1 : rigth_index]

if not elements_between:
    product_between = 0
else:
    product_between = 1
    for x in elements_between:
        product_between *= x

print(f"Сумма отрицательных чисел: {sum_negative}")
print(f"Сумма четных чисел: {sum_even}")
print(f"Сумма нечетных чисел: {sum_odd}")
print(f"Произведение элементов с индексами кратными 3: {product_index3}")
print(f"Произведение элементов между минимальным и максимальным элементом: {product_between}")












