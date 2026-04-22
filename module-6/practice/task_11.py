employees = [
    {
        "id": 1,
        "fio": "Иванов Иван Иванович",
        "phone": "+7 (900) 123-45-67",
        "email": "ivan.ivanov@firm.ru",
        "position": "Менеджер",
        "room": "305",
        "skype": "ivanov_skype"
    },
    {
        "id": 2,
        "fio": "Петрова Анна Сергеевна",
        "phone": "+7 (901) 234-56-78",
        "email": "anna.petrova@firm.ru",
        "position": "Бухгалтер",
        "room": "210",
        "skype": "petrova_a"
    }
]

print("Начальная база сотрудников:")
for emp in employees:
    print(emp)
print()

new_id = employees[-1]["id"] + 1

new_employee = {
    "id": new_id,
    "fio": "Сидоров Алексей Петрович",
    "phone": "+7 (902) 345-67-89",
    "email": "aleksey.sidorov@firm.ru",
    "position": "Инженер",
    "room": "401",
    "skype": "sidorov_alex"
}

employees.append(new_employee)
print("После добавления:")
for emp in employees:
    print(emp)
print()

i = 0
while i < len(employees):
    if employees[i]["id"] == 1:
        removed = employees.pop(i)
        print(f"Сотрудник {removed['fio']} (ID={removed['id']}) удалён.")
        break
    i += 1

print("После удаления:")
for emp in employees:
    print(emp)
print()

for emp in employees:
    if "Петрова" in emp["fio"]:
        print("Найден:", emp)
print()

i = 0
while i < len(employees):
    if employees[i]["id"] == 2:
        employees[i]["phone"] = "+7 (901) 999-88-77"
        employees[i]["position"] = "Главный бухгалтер"
        print(f"Данные сотрудника {employees[i]['fio']} обновлены.")
        break
    i += 1

for emp in employees:
    print(emp)
print()

for emp in employees:
    print(f"ID: {emp['id']}")
    print(f"ФИО: {emp['fio']}")
    print(f"Телефон: {emp['phone']}")
    print(f"Email: {emp['email']}")
    print(f"Должность: {emp['position']}")
    print(f"Кабинет: {emp['room']}")
    print(f"Skype: {emp['skype']}")