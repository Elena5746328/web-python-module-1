text = input("Введите текст: ")
reserved_words = input("Введите зарезервированные слова через пробел: ").split()
words = text.split()

for i in range(len(words)):
    if words[i].lower() in [word.lower() for word in reserved_words]:
        words[i] = words[i].upper()

result = " ".join(words)

print("Измененный текст:")
print(result)