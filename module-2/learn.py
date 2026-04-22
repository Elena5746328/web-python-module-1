# text = "row_1\nrow_2\nrow_3"
# Разбиение и объединение строк
# sl = text.splitlines()
# print(sl)
# f = text.split(", ") # Если пусто то разбиение по пробелам
# u = ", ".join(f) # Объединение элементов в строку
# print(f, u)

# Очистка
# print(text.strip()) # Очистка с левой и с правой части
# print(text.lstrip()) # Очистка левой части
# print(text.rstrip()) # Очистка правой части

# print("Пробелы: ", text.isspace())
# print("Только буквы и цифры: ", text.isalnum())
# print("Только цифры: ", text.isdigit())
# print("Только буквы: ", text.isalpha())
# print("Заглавные: ", text.isupper())
# print("Прописные: ", text.islower())

# Замена 
# print(text.replace("Hello", "Hi", 2))

# Поиск 
# print (text.index("j"))
# print(text.find("p"))

# Изменение регистра
# print(text.swapcase())
# print(text.upper())
# print(text.lower())
# print(text.capitalize())

# Срезы
# print(text[0:7])
# print(text[0:3]) 
# print(text[::-1])

# tuple_1_sum = ("b")
# tuple_2_sum = ("b",)
# print(tuple_1_sum, tuple_2_sum )

# Кортежи в цикле (интерирование)
# num_tuple = tuple(range(0,5))
# for num in num_tuple:
# for index, num in enumerate(num_tuple):
#     print(num)

# Методы кортежей
# numbers = (1,2,3,4,5,2,2)
# print(numbers.count(2)) # Считаем количество 
# print(numbers.index(2)) # Индекс первого исходного поиска

# Принадлежность
# f = ("apple", "banana")
# print("apple" in f)

# Повторение 
# pattern = ("a", "b")
# repeated = pattern * 2
# print(repeated)

# Объединение
# tuple1 = (1,2)
# tuple2 = (3,4)
# result = tuple1 + tuple2
# print(result)

# num1, _, num3, num4 = (1,2,3,4)
# print(num1, num3, num4)
# num1, *other, last_el = tuple(range(0, 11))
# tupl_1 = (1,2,3)
# tupl_2 = tuple(range(0, 11))
# tuple_3 = 1,2,3
# print(tupl_2[0])
# print(tupl_2[2:5])
# print(num1, other, last_el)