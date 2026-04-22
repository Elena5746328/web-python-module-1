fruits = ("banana", "apple", "bananamango", "mango", "strawberry-banana")
fruits_user = input("Введите название фрукта: ")
count = fruits.count(fruits_user)

part_element = 0
for item in fruits:
    if fruits_user in item:
        part_element += 1

print(f"Фрукт {fruits_user} встречается {count} раз")
print(f"Фрукт {fruits_user} ялвяется частью элемента {part_element}")