numbers = list(map(int, input("Введите элементы списка через пробел: ").split()))

sum_result = sum(numbers)
avg_result = sum_result / len(numbers)

print(f"Сумма всех элементов: {sum_result}")
print(f"Среднее арифметическое значение: {avg_result}")
