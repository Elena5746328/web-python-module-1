text = "в стране мифов, во времена магии, судьба великого королевства покоится на плечах мальчика. имя ему - Мерлин."
text_normalized = ". ".join(s.capitalize().strip() for s in text.split(". "))
print(text_normalized)
digit_count = 0
punct_count = 0
excl_count = 0
punctuation = "!,."

for char in text:
    if char.isdigit():
        digit_count += 1
    if char in punctuation:
        punct_count += 1
    if char == "!":
        excl_count += 1

print(f"Цифры: {digit_count}")
print(f"Знаки препинания: {punct_count}")
print(f"Восклицательные знаки: {excl_count}")





