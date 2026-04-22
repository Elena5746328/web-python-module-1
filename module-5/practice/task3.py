import random
tasks = []

for i in range(10):
    tasks.append({
        "id": f"t_{i}",
        "assignee": random.choice(["ivan", "olga", "petr", "anna", "oleg"]),
        "status": random.choice(["in_progress", "blocked", "in_review", "waiting_vendor"]),
        "days_in_status": random.randint(0, 10)
    })

long_in_progress = []
for task in tasks:
    if task["status"] == "in_progress" and task["days_in_status"] > 7:
        if task["assignee"] not in long_in_progress:
            long_in_progress.append(task["assignee"])

print(f"Исполнители, у которых есть задачи in_progress дольше 7 дней: {long_in_progress}")

status_by_assignee = {}
for task in tasks:
    assignee = task["assignee"]
    status = task["status"]
    if assignee not in status_by_assignee:
        status_by_assignee[assignee] = []
    if status not in status_by_assignee[assignee]:
        status_by_assignee[assignee].append(status)

status_count = {}
for assignee, statuses in status_by_assignee.items():
    for status in statuses:
        if status not in status_count:
            status_count[status] = 0
        status_count[status] += 1

unique_status = []
for status, count in status_count.items():
    if count == 1:
        unique_status.append(status)

print(f"Статусы, которые встречаются только у одного исполнителя: {unique_status}")

debt_by_assignee = {}
for task in tasks:
    if task ["status"] in ["in_progress", "blocked"]:
        assignee = task["assignee"]
        days = task["days_in_status"]
        if assignee not in debt_by_assignee:
            debt_by_assignee[assignee] = 0
        debt_by_assignee[assignee] += days

max_debt_assignee = None
max_debt = -1
for assignee, debt in debt_by_assignee.items():
    if debt > max_debt:
        max_debt = debt
        max_debt_assignee = assignee

print(f"Исполнитель с наибольшим суммарным долгом: {max_debt_assignee}, долг: {max_debt} дней")




    











