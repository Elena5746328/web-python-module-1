numbers = list(map(int, input("Введите элементы списка через пробел: ").split()))
number = int(input("Введите число для поиска: "))

count = numbers.count(number)
print(f"Число {number} встречается {count} раза")




