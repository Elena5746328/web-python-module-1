dictionary = [
    {"id": 1, "english": "hello", "french": "bonjour"},
    {"id": 2, "english": "world", "french": "monde"},
    {"id": 3, "english": "book", "french": "livre"}
]

print("Текущий словарь:")
for word in dictionary:
    print(word)
print()

new_id = dictionary[-1]["id"] + 1
english_word = "computer"
french_translation = "ordinateur"

dictionary.append({
    "id": new_id,
    "english": english_word,
    "french": french_translation
})

for word in dictionary:
    print(word)
print()

i = 0
while i < len(dictionary):
    if dictionary[i]["id"] == 2:
        dictionary.pop(i)
        print("Слово с ID=2 удалено.")
        break
    i += 1

print("Словарь после удаления:")
for word in dictionary:
    print(word)
print()

for word in dictionary:
    if word["english"] == "hello":
        print("Найденное слово:", word)
        break
print()

i = 0
while i < len(dictionary):
    if dictionary[i]["id"] == 1:
        dictionary[i]["french"] = "salut"
        print("Слово с ID=1 обновлено.")
        break
    i += 1

print("Словарь после обновления:")
for word in dictionary:
    print(word)
print()

print("Итоговый словарь:")
for word in dictionary:
    print(f"ID: {word['id']}, Английский: '{word['english']}', Французский: '{word['french']}'")
