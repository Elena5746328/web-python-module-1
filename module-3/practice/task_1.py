word = input("Введите слово: ")
char_count = {}

for char in word:
    char_count[char] = char_count.get(char, 0) + 1

print("результат: ") 
for char, count in char_count.items():
    print(f"{char} = {count}")
