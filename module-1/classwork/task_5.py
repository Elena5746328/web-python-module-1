number = int(input("Введите четырехзначное число: "))
reversed_number = 0

while number > 0:
    last_digit = number % 10
    reversed_number = reversed_number * 10 + last_digit
    number = number // 10

print("Перевернутое число:", reversed_number)