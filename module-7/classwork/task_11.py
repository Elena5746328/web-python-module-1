employees = []

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        current_emp = {}
        for line in f:
            line = line.strip()
            if line[:5] == "Имя: ":
                current_emp["name"] = line[5:]
            elif line[:8] == "Фамилия: ":
                current_emp["surname"] = line[8:]
            elif line[:8] == "Возраст: ":
                current_emp["age"] = line[8:]
            elif line[:10] == "Должность: ":
                current_emp["position"] = line[10:]
            elif line == "-" * 20:
                if current_emp:
                    employees.append(current_emp)
                    current_emp = {}

    if current_emp:
        employees.append(current_emp)

    print(f"Загружено {len(employees)} сотрудников из файла {filename}")

def save_data(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for emp in employees:
            f.write(f"Имя: {emp['name']}\n")
            f.write(f"Фамилия: {emp['surname']}\n")
            f.write(f"Возраст: {emp['age']}\n")
            f.write(f"Должность: {emp['position']}\n")
            f.write("-" * 20 + "\n")
    print(f"Данные сохранены в файл {filename}")

def save_search_results(results):
    filename = input("Введите имя файла для сохранения результатов: ")
    with open(filename, 'w', encoding='utf-8') as f:
        for emp in results:
            f.write(f"Имя: {emp['name']}\n")
            f.write(f"Фамилия: {emp['surname']}\n")
            f.write(f"Возраст: {emp['age']}\n")
            f.write(f"Должность: {emp['position']}\n")
            f.write("-" * 20 + "\n")
    print(f"Результаты поиска сохранены в файл {filename}")

def add_employee():
    print("\n--- Добавление нового сотрудника ---")
    name = input("Имя: ")
    surname = input("Фамилия: ")
    age = input("Возраст: ")
    position = input("Должность: ")

    employee = {
        "name": name, 
        "surname": surname,
        "age": age,
        "position": position
    }
    employees.append(employee)
    print("Сотрудник добавлен!")

def edit_employee():
    surname = input("Введите фамилию сотрудника для редактирования: ")
    found = False

    for emp in employees:
        if emp["surname"].lower() == surname.lower():
            print(f"\nНайден: {emp["name"]} {emp["surname"]}, {emp["age"]} лет, {emp["position"]}")
            emp["name"] = input(f"Новое имя ({emp["name"]}): ") or emp["name"]
            emp["surname"] = input(f"Новая фамилия ({emp["surname"]}): ") or emp["surname"]
            emp["age"] = input(f"Новый возраст ({emp["age"]}): ") or emp["age"]
            emp["position"] = input(f"Новая должность ({emp["position"]}): ") or emp["position"]
            found = True
            print("Данные обновлены")
            break

    if not found:
        print("Сотрудник не найден")

def delete_employee():
    surname = input("Введите фамилию для удаления: ")
    initial_count = len(employees)
    employees = [emp for emp in employees if emp["surname"].lower() != surname.lower()]

    if len(employees) < initial_count:
        print("Сотрудник удален")
    else:
        print("Сотрудник не найден")

def search_by_surname():
    surname = input("Введите фамилию для поиска: ")
    results = [emp for emp in employees if surname.lower() in emp["surname"].lower()]

    if results:
        print(f"\nНайден {len(results)} сотрудников:")
        for emp in results:
            print(f"{emp["name"]} {emp["surname"]}, {emp["age"]} лет, {emp["position"]}")
        save_choice = input("Сохранить результаты поиска в файл? (да/нет): ").lower()
        if save_choice in ["да"]:
            save_search_results(results)
    else:
        print("Сотрудники не найдены")

def show_by_age():
    age = input("Введите возраст: ")
    results = [emp for emp in employees if emp["age"] == age]

    if results:
        print(f"\nСотрудники возраста {age} лет:")
        for emp in results:print(f"{emp["name"]} {emp["surname"]}, {emp["position"]}")
        save_choice = input("Сохранить результаты поиска в файл? (да/нет): ").lower()
        if save_choice in ["да"]:
            save_search_results(results)
    else:
        print(f"Сотрудники возраста {age} не найдены")

def show_by_first_letter():
    letter = input("Введите первую букву фамилии: ").lower()
    results = [emp for emp in employees if emp["surname"] and emp["surname"][0].lower() == letter]

    if results:
        print(f"\nСотрудники с фамилией на букву '{letter}': ")
        for emp in results:
            print(f"{emp["name"]} {emp["surname"]}, {emp["age"]} лет, {emp["position"]}")
        save_choice = input("Сохранить результаты поиска в файл? (да/нет): ").lower()
        if save_choice in ["да"]:
            save_search_results(results)
    else:
        print(f"Сотрудники с фамилией на '{letter}' не найдены")

def show_all():
    if employees:
        print("\n--- Все сотрудники ---")
        count = 1
        for emp in employees:
            print(f"{count}. {emp["name"]} {emp["surname"]}, {emp["age"]} лет, {emp["position"]}")
            count += 1
    else:
            print("Список сотрудников пуст")