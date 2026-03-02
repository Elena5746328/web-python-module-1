def print_menu():
    print("\nМеню:")
    print("1. Отсортировать по идентификационным кодам")
    print("2. Отсортировать по номерам телефона")
    print("3. Вывести список пользователей с кодами и телефонами")
    print("4. Выход")

def sort_by_ids(ids, phones):
    n = len(ids)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ids[j] > ids[j + 1]:
                ids[j], ids[j + 1] = ids[j + 1], ids[j]
                phones[j], phones[j + 1] = phones[j + 1], phones[j]
    return ids, phones

def sort_by_phones(ids, phones):
    n = len(phones)
    for i in range(n):
        for j in range(0, n - i - 1):
            if phones[j] > phones[j + 1]:
                ids[j], ids[j + 1] = ids[j + 1], ids[j]
                phones[j], phones[j + 1] = phones[j + 1], phones[j]
    return ids, phones

def display_list(ids, phones):
    if not ids:
        print("Список пуст!")
        return
    print("\nСписок пользователей:")
    print("-! * 30")
    for i in range(len(ids)):
        print(f"{i + 1}. ID: {ids[i]}, Телефон: {phones[i]}")
    print("-" * 30)

identification_ids = [103, 101, 105, 102, 104]
phone_numbers = [79123456789, 79234567890, 79345678901, 79456789012, 79567890123]

print("Программа «Справочник» запущена!")
print_menu()
choice = input("Выберите пункт меню (1–4): ")

if choice == '1':
    identification_ids, phone_numbers = sort_by_ids(identification_ids, phone_numbers)
    print("Список отсортирован по идентификационным кодам!")
elif choice == '2':
    identification_ids, phone_numbers = sort_by_phones(identification_ids, phone_numbers)
    print("Список отсортирован по номерам телефона!")
elif choice == '3':
    display_list(identification_ids, phone_numbers)
elif choice == '4':
    print("Выход из программы. До свидания!")
else:
    print("Неверный выбор! Пожалуйста, выберите число от 1 до 4.")

