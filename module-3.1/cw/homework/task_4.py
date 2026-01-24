list1 = [4, 9, -2, 6, 8, 7, -1, 0, 3, -5]
list2 = [23, -65, 99, 82, -39, 12, 33, -44, 26, 51]

combined = list1 + list2

combined_no_duplicates = list(set(list1 + list2))

common_elements = list(set(list1) & set(list2))

unique_list1 = set(list1) - set(list2)
unique_list2 = set(list2) - set(list1)
unique_elements = list(unique_list1) + list(unique_list2)

min_max = [min(list1), max(list1), min(list2), max(list2)]

print(f"Объединенный список: {combined}")
print(f"Объединенный список без повторений: {combined_no_duplicates}")
print(f"Общие элементы: {common_elements}")
print(f"Уникальные элементы каждого списка: {unique_elements}")
print(f"Минимальные и максимальные значение каждого списка: {min_max}")