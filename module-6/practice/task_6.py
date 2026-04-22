clients = [
    (1, "111", "a@x.com"),
    (2, "111", "b@x.com"),
    (3, "222", "c@x.com"),
    (4, "333", "c@x.com"),
    (5, "444", "d@x.com")
]

phone_duplicates = {}
email_duplicates = {}
for id, phone, email in clients:
    phone_duplicates.setdefault(phone, set()).add(id)
    email_duplicates.setdefault(email, set()).add(id)
print(phone_duplicates)
print(email_duplicates)

duplicates = []
for o in (phone_duplicates, email_duplicates):
    for ids in o.values():
        if len(ids) > 1:
            duplicates.append(ids)
print(duplicates)

duplicate_ids = set()
for m in duplicates:
    duplicate_ids |= m

clean_clients = []
for client in clients:
    if client[0] not in duplicate_ids:
        clean_clients.append(client[0])

len(clean_clients)
print(clean_clients)







    





