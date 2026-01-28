fruits = ("яблоко", "банан", "яблоко", "апельсин", "груша", "яблоко")
fruits_user = input("Введите название фрукта: ")
count = fruits.count(fruits_user)
print(f"Фрукт {fruits_user} встречается {count} раза")