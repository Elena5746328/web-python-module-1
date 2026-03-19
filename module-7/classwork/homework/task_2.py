char_count = 0
line_count = 0
vowel_count = 0
consonant_count = 0
digit_count = 0

input_filename = input("Введите имя исходного файла: ")
output_filename = input("Введите имя выходного файла для статистики: ")

with open(input_filename, "r", encoding="utf-8") as file:
    for line in file:
        line_count += 1
        char_count += len(line)

        for char in line:
            if char.isdigit():
                digit_count += 1
            elif char.lower():
                vowel_count += 1
            else:
                consonant_count += 1

with open(output_filename, "w", encoding="utf-8") as file:
    file.write("Статистика по файлу\n")
    file.write("=" * 30 + "\n\n") 

    file.write(f"Количество строк: {line_count}\n")
    file.write(f"Количество символов: {char_count}\n")
    file.write(f"Количество гласных букв: {vowel_count}\n")
    file.write(f"Количество согласных букв: {consonant_count}\n")
    file.write(f"Количество цифр: {digit_count}\n")

print(f"Статистика успешно подсчитана и сохранена в файл: {output_filename}")


