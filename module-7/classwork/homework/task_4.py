lines = []
max_length = 0
longest_line = ""

filename = input("Введите имя файла: ")

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.strip()
        lines.append(clean_line)

for line in lines:
    current_length = len(line)
    if current_length > max_length:
        max_length = current_length
        longest_line = line

print(f"Длина самой длинной строки: {max_length}")
print(f"Самая длиннная строка: '{longest_line}'")