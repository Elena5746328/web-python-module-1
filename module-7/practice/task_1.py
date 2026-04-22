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

# 1
with open("inventory.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(operations_to_file))

# 2
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

# 3
total_count = {}
total_in = {}
total_out = {}
product_dates = {}

for operation in operations:
   date, product, operation_type, quantity = operation["date"], operation["product"], operation["operation_type"], operation["quantity"]

   total_count.setdefault(product, 0)
   total_in.setdefault(product, 0)
   total_out.setdefault(product, 0)
   product_dates.setdefault(product, set()).add(date)
   if operation_type == "IN":
      total_count[product] += quantity
      total_in[product] += quantity

   else:
      total_count[product] -= quantity
      total_out[product] += quantity
   
for key, value in total_count.items():
   print(f"На складе {key}: {value}")
print("-"*20)
for key, value in total_in.items():
   print(f"Приехало {key}: {value}")
print("-"*20)
for key, value in total_out.items():
   print(f"Отгружено {key}: {value}")

# 4
negative_products = []
for product, amount in total_count.items():
   if amount < 0:
      negative_products.append(product)
print(f"Ошибка учета: {negative_products}")

not_incoming_but_outgoing = []
for product, outgoing in total_out.items():
   if outgoing > 0 and product not in total_in:
      not_incoming_but_outgoing.append(product)
print(f"Которые ни разу не поступали, но отгружались: {not_incoming_but_outgoing}")

# 5
max_in_product = None
max_in_quantuty = -1
for product, quantity in total_in.items():
   if quantity > max_in_quantuty:
      max_in_product = product
      max_in_quantuty = quantity

max_out_product = None
max_out_quantuty = -1
for product, quantity in total_out.items():
   if quantity > max_in_quantuty:
      max_in_product = product
      max_in_quantuty = quantity

# 6
apple_dates = product_dates.get("яблоко", set())
print(f"Когда происходили операции с яблоком: {apple_dates}")

# 7
with open("report.txt", "w", encoding="utf-8") as report_file:
   report_file.write("Отчет по складу")
   report_file.write("=" * 40 + "\n\n")

   report_file.write("Итоговые остатки")
   for porduct, count in sorted(total_count.items()):
      report_file.write(f"{product}: {count}\n")
   report_file.write("\n")

   report_file.write("Общее поступление\n")
   for porduct, qty in sorted(total_in.items()):
      report_file.write(f"{product}: {qty}\n")
   report_file.write("\n")

   report_file.write("Общая отгрузка")
   for porduct, count in sorted(total_count.items()):
      report_file.write(f"{product}: {count}\n")
   report_file.write("\n")

   report_file.write("Товары с отрицательным остатком:\n")
   if negative_products:
      for product in negative_products:
         report_file.write(f"{product}: {total_count[product]}")
   else:
      report_file.write("\n")

   report_file.write("Товары без поступлений, но с отгрузкой:\n")
   if not_incoming_but_outgoing:
         report_file.write(f"{product}: отгружено {total_count[product]}\n")
   else:
      report_file.write("\n")

   report_file.write("Товар с максимальным поступлением:\n")
   if max_in_product:
         report_file.write(f"{max_in_product}:{max_in_quantuty}\n")
   else:
      report_file.write("\n")

   report_file.write("Товар с максимальной отгрузкой:\n")
   if max_in_product:
         report_file.write(f"{max_out_product}:{max_out_quantuty}\n")
   else:
      report_file.write("\n")

   report_file.write("Даты операций с яблоком::\n")
   if apple_dates:
      for date in sorted(apple_dates):
         report_file.write(f"{date}\n")
print("Отчет успешно записан в файл 'report.txt'")

   

   

   



   










      










    
    
    
    
    
    
    

    

      
