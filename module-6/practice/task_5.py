network = {
    "Me": {"Alice", "Bob"},
    "Alice": {"Me", "Chalie", "Bob"},
    "Bob": {"Me", "David", "Eve"},
    "Charlie": {"Alice"},
    "David": {"Alice", "Bob"},
    "Eva": {"Bob"}
}

user = "Me"

friends_of_user = list(network[user])
friends_of_friends = []
for friend in friends_of_user:
    for friends_of_friend in network[friend]:
        if friends_of_friend not in friends_of_friends:
            friends_of_friends.append(friends_of_friend)


result = []
for person in friends_of_friends:
    if person != user and person not in friends_of_user:
        result.append(person)

print(f"Друзья друзей, которых нет в списке: {result}")

        


