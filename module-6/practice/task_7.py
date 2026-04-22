logs = [
    ("ivan", "d1", "login"),
    ("ivan", "d1", "view"),
    ("ivan", "d2", "login"),
    ("olga", "d1", "login"),
    ("petr", "d2", "error"),
    ("anna", "d1", "login"),
    ("anna", "d2", "view")
]

user_action_count = {}
user_actions = {}
user_days = {}
for user, day, action in logs:
    user_action_count[user] = user_action_count.get(user, 0) + 1
    if user not in user_actions:
        user_actions[user] = set()
    user_actions[user].add(action)
    if user not in user_days:
        user_days[user] = set()
    user_days[user].add(day)
print(user_action_count)
print(user_actions)
print(user_days)

users_active = set()
for user, days in user_days.items():
    if len(days) > 1:
        users_active.add(user)
print(users_active)

day_activity = {}
for user, day, action in logs:
    day_activity[day] = day_activity.get(day, 0) + 1
    













