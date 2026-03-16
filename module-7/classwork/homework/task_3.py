lines = []
output_lines = []

input_filename = input("Введите имя исходного файла: ")
output_filename = input("ВВедите имя выходного файла: ")

with open(input_filename, "r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.strip()
        lines.append(clean_line)

if lines:
    output_lines = lines[:-1]
else:
    output_lines = []

with open(output_filename, "w", encoding="utf-8") as file:
    for line in output_lines:
        file.write(line + "\n")

print(f"Последняя строка удаленаю Результат сохранен в файл: {output_filename}")