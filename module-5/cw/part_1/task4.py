logs = [
    ("ivan", "day", 8),
    ("ivan", "night", 4),
    ("olga", "day", 6),
    ("petr", "night", 7),
    ("anna", "day", 4),
    ("anna", "day", 3)
]

person_shifts = {}
for log in logs:
    if log[0] not in person_shifts:
        person_shifts[log[0]] = set()
    person_shifts[log[0]].add(log[1])

persons = []
for person in person_shifts:
    if len(person_shifts[person]) == 2:
        persons.append(person)

print(f"Сотрудники, которые работали в разных сменах: {persons}")

shifts_sum = {}




    