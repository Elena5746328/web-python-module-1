def print_grades(grades):
    print("Оценки студента:", grades)

def retake_exam(grades):
    index = int(input("Введите номер оценки для пересдачи (1-10): ")) - 1
    if 0 <= index < len(grades):
        new_grade = int(input("Введите новую оценку (1-12): "))
        if 1 <= new_grade <= 12:
            grades[index] = new_grade
            print("Оценка успешно обновлена!")
        else:
            print("Ошибка: оценка должна быть от 1 до 12.")
    else:
        print("Ошибка: неверный номер оценки.")

def check_scholarship(grades):
    average = sum(grades) / len(grades)
    if average >= 10.7:
        print(f"Средний балл: {round(average, 2)}. Стипендия ВЫХОДИТ!")
    else:
        print(f"Средний балл: {round(average, 2)}. Стипендия НЕ выходит.")

def sort_grades(grades):
    choice = input("Сортировать по возрастанию (в) или убыванию (у)? ")
    sorted_grades = sorted(grades, reverse=(choice.lower() == 'у'))
    print("Отсортированные оценки:", sorted_grades)

def main():
    grades = []
    print("Введите 10 оценок студента (от 1 до 12):")
    for i in range(10):
        grade = int(input(f"Оценка {i + 1}: "))
        if 1 <= grade <= 12:
            grades.append(grade)
        else:
            print("Предупреждение: оценка вне диапазона 1–12. Она всё равно будет сохранена.")
            grades.append(grade)

    print("\n" + "="*40)
    print("МЕНЮ: УСПЕВАЕМОСТЬ")
    print("="*40)
    print("1. Вывод оценок")
    print("2. Пересдача экзамена")
    print("3. Выходит ли стипендия?")
    print("4. Вывод отсортированного списка оценок")
    print("5. Выход")
    print("-"*40)

    choice = input("Выберите действие (1-5): ")

    if choice == '1':
        print_grades(grades)
    elif choice == '2':
        retake_exam(grades)
    elif choice == '3':
        check_scholarship(grades)
    elif choice == '4':
        sort_grades(grades)
    elif choice == '5':
        print("До свидания!")
    else:
        print("Неверный выбор.")

main()
