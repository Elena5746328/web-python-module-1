numbers = [3, -5, 0, 9, -3, 0, 2, -6, 7]

min_val = numbers[0]
max_val = numbers[0]
negatiive_count = 0
positive_count = 0
zero_count = 0

for num in numbers:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

    if num < 0:
        negatiive_count += 1
    elif num > 0:
        positive_count += 1
    else:
        zero_count += 1

print(f"Список: {numbers}")
print(f"Минимальный элемент: {min_val}")
print(f"Максимальный элемент: {max_val}")
print(f"Количество отрицательных элементов: {negatiive_count}")
print(f"Количество положительных элементов: {positive_count}")
print(f"Количество нулей: {zero_count}")
