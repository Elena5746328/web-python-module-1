def main_directory():
    codes = [103, 101, 102, 105, 104]
    phones = ["+79001112233", "+79004445566", "+79007778899", "+79002223344", "+79005556677"]

    users = list(zip(codes, phones))

    while True:
        print("\n--- СПРАВОЧНИК ---")
        print("1. Отсортировать по идентификационным кодам")
        print("2. Отсортировать по номерам телефона")
        print("3. Вывести список пользователей с кодами и телефонами")
        print("4. Выход")
        choice = input("Выберите пункт меню(1-4): ")

        if choice == "1":
            users.sort(key=lambda x: x[0])
            print("Отсортировано по идентификационным кодам")

        elif choice == "2":
            users.sort(key=lambda x: x[1])
            print("Отсортировано по номерам телефона")

        elif choice == "3":
            print("Список пользователей:")
            for code, phone in users:
                print(f"Код: {code}, Телефон: {phone}")

        elif choice == "4":
            print("Выход из программы")
            break

        else:
            print("Неверный пункт меню")

main_directory()