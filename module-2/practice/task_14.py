expression = input("Введите арифметические выражение (например, 23+12): ")

if "+" in expression:
    a, b = expression.split("+")
    result = float(a) + float(b)
elif "-" in expression:
    a, b = expression.split("-")
    result = float(a) - float(b)
elif "*" in expression:
    a, b = expression.split("*")
    result = float(a) * float(b)
elif "/" in expression:
    a, b = expression.split("/")
    if float(b) == 0:
        print("Ошибка: деление на ноль")
    else:
        result = float(a) / float(b)

print(f"Результат: {result}")



    
