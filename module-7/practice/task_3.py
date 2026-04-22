file1_lines = []
file2_lines = []

file1_name = input("Введите имя первого файла: ")
file2_name = input("Введите имя второго файла: ")

with open(file1_name, "r", encoding="utf-8") as file:
    for line in file:
        file1_lines.append(line.strip())

with open(file2_name, "r", encoding="utf-8") as file:
    for line in file:
        file2_lines.append(line.strip())

print("\nРезултат сравнения файлов")
print("=" * 40)

max_lines = max(len(file1_lines), len(file2_lines))
mismatch_found = False

for i in range(max_lines):
    line1 = file1_lines[i] if i < len(file1_lines) else "[Стройка отсутствует]\n"
    line2 = file2_lines[i] if i < len(file2_lines) else "[Стройка отсутствует]\n"

    if line1 != line2:
        mismatch_found = True
        print(f"\nСтрока {i + 1}:")
        print(f"Файл 1: {line1.strip()}")
        print(f"Файл 2: {line2.strip()}")

if not mismatch_found:
    print("Все строки в файлах совпадают")
else:
    mismatch_count = 0
    for i in range(max_lines):
        line1 = file1_lines[i] if i < len(file1_lines) else None
        line2 = file2_lines[i] if i < len(file2_lines) else None

        if line1 is None or line2 is None:
            mismatch_count += 1
        elif line1 != line2:
            mismatch_count += 1
    print(f"\nСравнение завершено. Найдено {mismatch_count} несовпадений")
