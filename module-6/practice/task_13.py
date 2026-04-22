payments = [
    ("ivan", 100),
    ("ivan", -30),
    ("ivan", -20),
    ("olga", 200),
    ("petr", -50),
]

balance = {}
operation_count = {}

for user, amount in payments:
    if user in balance:
        balance[user] += amount
    else:
        balance[user] = amount

    if user in operation_count:
        operation_count[user] += 1
    else:
        operation_count[user] = 1

print("Баланс по каждому пользователю:")
for user, bal in balance.items():
    print(f"{user}: {bal}")

print("\nПользователи с отрицательным балансом:")
negative_balance_users = []
for user, bal in balance.items():
    if bal < 0:
        negative_balance_users.append(user)
        print(user)

if not negative_balance_users:
    print("Нет пользователей с отрицательным балансом")

print("\nПользователи с более чем 2 операциями:")
high_operation_users = []
for user, count in operation_count.items():
    if count > 2:
        high_operation_users.append(user)
        print(f"{user} ({count} операций)")

if not high_operation_users:
    print("Нет пользователей с более чем 2 операциями")