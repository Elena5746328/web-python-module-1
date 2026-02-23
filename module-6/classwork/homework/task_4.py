books = [
    (1, "Жестокий принц", "	Холли Блэк", "роман", "2018", "480", "Эксмо"),
    (2, "Злой король", "Холли Блэк", "роман", "2018", "448", "Эксмо"),
    (3, "Королева ничего", "Холли Блэк", "роман", "2018", "480", "Эксмо")
    ]

for book in books:
    print(book)
print()

new_id = books[-1][0] + 1
title = "Как король Эльфхейма научился ненавидеть истории"
author = "Холли Блэк"
genre = "Роман"
year = "2021"
pages = "192"
publisher = "Эксмо"

books.append((new_id, title, author, genre, year, pages, publisher))
for book in books:
    print(book)
print()

i = 0
while i < len(books):
    if books[i][0] == 1:
        books.pop(i)
        print("Книга с ID=1 удалена.")
        break
    i += 1

for book in books:
    print(book)
print()

for book in books:
    if "Королева ничего" in book[1]:
        print("Найденная книга:", book)
print()

i = 0
while i < len(books):
    if books[i][0] == 2:
        books[i] = (2, "Злой король (новое издание)", "Холли Блэк", "роман", "2022", "480", "Эксмо")
        print("Книга с ID=2 обновлена.")
        break
    i += 1

for book in books:
    print(book)
print()

for book in books:
    print(f"ID: {book[0]}, Название: «{book[1]}», Автор: {book[2]}, "
          f"Жанр: {book[3]}, Год: {book[4]}, Страниц: {book[5]}, Издательство: {book[6]}")