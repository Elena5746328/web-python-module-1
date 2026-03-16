lines = []
word_count = 0

filename = input("Введите имя файла: ")
search_word = input("Какое слово нужно найти: ")

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())

for line in lines:
    words = line.split()
    word_count += words.count(search_word)

print(f"Слово '{search_word}' встречается {word_count} раз в файле '{filename}'")