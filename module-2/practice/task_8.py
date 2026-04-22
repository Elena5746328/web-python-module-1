text = input("Введите строку: ")
old_world = input("Введите слово для поиска: ")
new_world = input("Введите слово для замены: ")

result = text.replace(old_world, new_world)

print(f"Результат замены: {result}")