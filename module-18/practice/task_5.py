def main_books():
    titles = ["Война и мир", "Преступление и наказание", "Мастер и Маргарита", "1984", "Маленький принц"]
    years = [1869, 1866, 1967, 1949, 1943]

    books = list(zip(titles, years))

    while True:
        print("\n--- КНИГИ ---")
        print("1. Отсортировать по названию книг")
        print("2. Отсортировать по годам выпуска")
        print("3. Вывести список книг с названиями и годами выпуска")
        print("4. Выход")
        choice = input("Выберите пункт меню (1–4): ")

        if choice == "1":
            books.sort(key=lambda x: x[0].lower())
            print("Отсортировано по названию книг.")

        elif choice == "2":
            books.sort(key=lambda x: x[1])
            print("Отсортировано по годам выпуска.")

        elif choice == "3":
            print("Список книг:")
            for title, year in books:
                print(f"Название: {title}, Год выпуска: {year}")

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Неверный пункт меню.")

main_books()
