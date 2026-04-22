logs = [
    ("ivan", 8), ("ivan", 10),
    ("olga", 20),
    ("petr", 45),
]

total_hours = {}
for employee, hours in logs:
    if employee in total_hours:
        total_hours[employee] += hours
    else:
        total_hours[employee] = hours

print("Суммарные часы по сотрудникам:")
for employee, total in total_hours.items():
    print(f"{employee}: {total} часов")

print("\nАнализ переработок и недоработок:")

overtime = []
underwork = []

for employee, total in total_hours.items():
    if total > 40:
        overtime.append((employee, total))
    elif total < 20:
        underwork.append((employee, total))

if overtime:
    print("Переработка (> 40 часов):")
    for emp, hours in overtime:
        print(f"{emp}: {hours} часов")
    else:
        print("Переработок нет")

if underwork:
    print("Недоработка (< 20 часов):")
    for emp, hours in underwork:
        print(f"{emp}: {hours} часов")
else:
    print("Недоработок нет")