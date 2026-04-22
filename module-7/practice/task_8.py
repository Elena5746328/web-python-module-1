lines = []
output_lines = []

filename = input("Введите имя файла: ")
search_word = input("Какое слово нужно найти: ")
replace_word = input("На что заменить: ")

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())

for line in lines:
    new_line = line.replace(search_word, replace_word)
    output_lines.append(new_line)

output_filename = "modified" + filename
with open(output_filename, "w", encoding="utf-8") as file:
    for line in output_lines:
        file.write(line + "\n")
        
print(f"Замена завершена. Результат сохранен в файл: {output_filename}")