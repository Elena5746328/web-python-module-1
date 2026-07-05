def get_grades():
    grades = []
    print("Введите 10 оценок студента (от 1 до 12):")
    while len(grades) < 10:
        try:
            grade = int(input(f"Оценка {len(grades) + 1}: "))
            if 1 <= grade <= 12:
                grades.append(grade)
            else:
                print("Оценка должна быть от 1 до 12.")
        except ValueError:
            print("Пожалуйста, введите целое число.")
    return grades


def show_grades(grades):
    print("Оценки студента:", grades)


def retake_exam(grades):
    try:
        index = int(input("Введите номер оценки для пересдачи (1–10): ")) - 1
        if 0 <= index < len(grades):
            new_grade = int(input("Введите новую оценку (1–12): "))
            if 1 <= new_grade <= 12:
                grades[index] = new_grade
                print("Оценка обновлена.")
            else:
                print("Некорректная оценка.")
        else:
            print("Неверный номер оценки.")
    except ValueError:
        print("Пожалуйста, вводите числа.")


def check_scholarship(grades):
    average = sum(grades) / len(grades)
    print(f"Средний балл: {average:.2f}")
    if average >= 10.7:
        print("Стипендия положена.")
    else:
        print("Стипендия не положена.")


def sort_grades(grades):
    choice = input("Сортировать по возрастанию (1) или по убыванию (2)? ")
    if choice == "1":
        sorted_grades = sorted(grades)
        print("Отсортировано по возрастанию:", sorted_grades)
    elif choice == "2":
        sorted_grades = sorted(grades, reverse=True)
        print("Отсортировано по убыванию:", sorted_grades)
    else:
        print("Неверный выбор.")


def main():
    grades = get_grades()
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Вывод оценок")
        print("2. Пересдача экзамена")
        print("3. Выходит ли стипендия")
        print("4. Вывод отсортированного списка оценок")
        print("5. Выход")
        choice = input("Выберите пункт меню (1–5): ")

        if choice == "1":
            show_grades(grades)
        elif choice == "2":
            retake_exam(grades)
        elif choice == "3":
            check_scholarship(grades)
        elif choice == "4":
            sort_grades(grades)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню.")

main()
