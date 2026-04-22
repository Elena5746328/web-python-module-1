dict = {}
count = int(input("Сколько пар 'ключей-значения' вы хотите создать? "))

for i in range(count):
    key = input("Введите названия ключа: ")
    value = input("Введите значение: ")
    dict[key] = value

print(dict)   


