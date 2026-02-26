purchases = [
    {"user": "Алиса", "items": ["яблоко", "банан"],          "price": 120, "timestamp": 1},
    {"user": "Боб",   "items": ["банан"],                    "price": 50,  "timestamp": 2},
    {"user": "Алиса", "items": ["апельсин", "яблоко"],       "price": 150, "timestamp": 5},
    {"user": "Боб",   "items": ["яблоко", "апельсин"],       "price": 130, "timestamp": 6},
    {"user": "Алиса", "items": ["банан", "банан"],           "price": 70,  "timestamp": 15},
    {"user": "Боб",   "items": ["банан"],                    "price": 40,  "timestamp": 25},
]

purchase_count = {}
total_spent = {}
unique_items = {}
item_count = {}

for purchase in purchases:
    user = purchase["user"]
    items = purchase["items"]
    price = purchase["price"]

    purchase_count[user] = purchase_count.get(user, 0) + 1

    total_spent[user] = total_spent.get(user, 0) + price

    if user not in unique_items:
        unique_items[user] = set()
    unique_items[user].update(items)

    item_count[user] = item_count.get(user, 0) + len(items)

print("1. Количество покупок по пользователям:")
for user, count in purchase_count.items():
    print(f"{user}:{count}")

print("\n2. Сумма потраченных денег по пользователям:")
for user, amount in total_spent.items():
    print(f"{user}:{amount} рублей")

print("\n3. Уникальные товары по пользователям:")
for user, items in unique_items.items():
    print(f"{user}:{sorted(items)}")

print("\n3. Общее количество товаров по пользователям:")
for user, count in item_count.items():
    print(f"{user}:{count} штук")

item_frequency = {}
for purchase in purchases:
    for item in purchase["items"]:
        item_frequency[item] = item_frequency.get(item, 0) + 1

most_frequent_item = None
max_frequency = 0
for item, frequency in item_frequency.items():
    if frequency > max_frequency:
        max_frequency = frequency
        most_frequent_item = item

print(f"\n4. Самый популярный товар: {most_frequent_item} (куплен {max_frequency} раз)")

max_spent_user = None
max_spent_amount = 0
max_items_user = None
max_items_count = 0

for user in purchase_count:
    if total_spent[user] > max_spent_amount:
        max_spent_amount = total_spent[user]
        max_spent_user = user

    if item_count[user] > max_items_count:
        max_items_count = item_count[user]
        max_items_user = user

print(f"\5.Больше всего потратил: {max_spent_user} ({max_spent_amount} рублей)")
print(f"Больше всего товаров купил: {max_items_user} ({max_items_count} штук)")

max_gaps = {}
user_timestamps = {}

for purchase in purchases:
    user = purchase["user"]
    timestamp = purchase["timestamp"]
    if user not in user_timestamps:
        user_timestamps[user] = []
    user_timestamps[user].append(timestamp)

for user, timestamps in user_timestamps.items():
    sorted_timestamps = sorted(timestamps)
    if len(sorted_timestamps) < 2:
        max_gap = 0
    else:
        max_gap = max(sorted_timestamps[i] - sorted_timestamps[i-1]
                   for i in range(1, len(sorted_timestamps)))
    max_gaps[user] = max_gap

print("\n6. Самые большие перерывы между покупками (по пользователям):")
for user, gap in max_gaps.items():
    print(f"{user}: {gap} единиц времени")




