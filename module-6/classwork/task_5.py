network = {
    "Me": {"Alice", "Bob"},
    "Alice": {"Me", "Chalie", "Bob"},
    "Bob": {"Me", "David", "Eve"},
    "Charlie": {"Alice"},
    "David": {"Alice", "Bob"},
    "Eva": {"Bob"}
}

user = "Me"

friends_of_user = network[user]
friends_of_friends = []
for i in friends_of_user:
    friends_of_friends.update(network[i])









