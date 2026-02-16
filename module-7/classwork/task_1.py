"""
ЗАДАЧА: Учёт инвентаря на складе

Формат строки:
дата,товар,тип,количество

Операции:
2024-01-01,яблоко,IN,50
2024-01-02,банан,IN,30
2024-01-03,яблоко,OUT,10
2024-01-03,груша,OUT,5
2024-01-04,груша,IN,20
2024-01-05,банан,OUT,40
2024-01-06,яблоко,OUT,5

Типы операций:
- IN  : поступление товара
- OUT : отгрузка товара

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Создать файл inventory.txt с операциями склада

2. Прочитать файл и загрузить все операции.

3. Для каждого товара:
   - посчитать итоговое количество на складе
   - посчитать общее количество поступивших единиц
   - посчитать общее количество отгруженных единиц

4. Найти товары:
   - у которых итоговое количество < 0 (ошибка учёта)
   - которые ни разу не поступали, но отгружались

5. Найти товар с:
   - максимальным количеством поступлений
   - максимальным количеством отгрузок

6. Сформировать множество всех дат,
   когда происходили операции с товаром "яблоко".

7. Записать подробный отчёт в файл report.txt.

- ОТЧЁТ ПО СКЛАДУ
- Итоговые остатки
- Общее поступление
- Общая отгрузка
- Товары с отрицательным остатком:
- Товары без поступлений, но с отгрузкой:
- Товар с максимальным поступлением:
- Товар с максимальной отгрузкой:
- Даты операций с яблоком:
"""

operations_to_file = [
"2024-01-01,яблоко,IN,50",
"2024-01-02,банан,IN,30",
"2024-01-03,яблоко,OUT,10",
"2024-01-03,груша,OUT,5",
"2024-01-04,груша,IN,20",
"2024-01-05,банан,OUT,40",
"2024-01-06,яблоко,OUT,5"
]

with open("inventory.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(operations_to_file))

operations = []
with open("inventory.txt", "r", encoding="utf-8") as f:
   for line in f:
      date, product, operation_type, quantity = line.split(",")

      operations.append({
         "date": date,
         "product": product,
         "operation_type": operation_type,
         "quantity": int(quantity)
      })

print(operations)

total_count = {}
total_in = {}
total_out = {}

for operation in operations:
   date, product, operation_type = operation["date"], operation["product"], operation["operation_type"], operation["quantity"]

   total_count.setdefault(product, 0)
   total_in.setdefault(product, 0)
   total_out.setdefault(product, 0)
   if operation_type == "IN":
      total_count[product] += quantity
      total_in[product] += quantity

   else:
      total_count[product] -= quantity
      total_out[product] -= quantity





      










    
    
    
    
    
    
    

    

      
