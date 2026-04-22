car = ("Audi", "BMW", "Audi", "Hyundai", "Audi", "Mazda", "Audi", "Toyota", "Audi", "Volvo")
replacement_car = input("Введите название производителя для замены: ")
replacement_word = input("Введите слово для замены: ")

new_list = []

for item in car:
    if item == replacement_car:
        new_list.append(replacement_word)
    else:
        new_list.append(item)

new_tuple = tuple(new_list)

print(f"Кортеж после замены: {new_tuple}")

