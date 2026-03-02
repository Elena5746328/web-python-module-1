def print_books(titles, years):
    print("\nСписок книг:")
    print("-! * 40")
    for i in range(len(titles)):
        print(f"Название: {titles[i]}, Год выпуска: {years[i]}")
    print()

def sort_by_title(titles, years):
    n = len(titles)
    for i in range(n):
        for j in range(0, n - i - 1):
            if titles[j] > titles[j + 1]:
                titles[j], titles[j + 1] = titles[j + 1], titles[j]
                years[j], years[j + 1] = years[j + 1], years[j]
    return titles, years

def sort_by_year(titles, years):
    n = len(years)
    for i in range(n):
        for j in range(0, n - i - 1):
            if years[j] > years[j + 1]:
                years[j], years[j + 1] = years[j + 1], years[j]
                titles[j], titles[j + 1] = titles[j + 1], titles[j]
    return titles, years

def main():
    book_titles = [
        "Война и мир",
        "Преступление и наказание",
        "Мастер и Маргарита",
        "1984",
        "Гарри Поттер и философский камень"
    ]
    book_years = [1869, 1866, 1966, 1949, 1997]
    program_running = True

    while program_running:
        print("\nМеню:")
        print("1. Отсортировать по названию книг")
        print("2. Отсортировать по годам выпуска")
        print("3. Вывести список книг с названиями и годами выпуска")
        print("4. Выход")

        choice = input("\nВыберите пункт меню (1-4): ")

        if choice == '1':
            sort_by_title(book_titles, book_years)
            print("Книги отсортированы по названию!")

        elif choice == '2':
            sort_by_year(book_titles, book_years)
            print("Книги отсортированы по годам выпуска!")

        elif choice == '3':
            print_books(book_titles, book_years)

        elif choice == '4':
            print("Выход из программы. До свидания!")
            program_running = False

        else:
            print("Неверный выбор! Пожалуйста, выберите пункт от 1 до 4.")

main()