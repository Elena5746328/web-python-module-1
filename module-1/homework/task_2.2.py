salary = float(input("Введите зарплату за месяц: "))
credit_paument = float(input("Введите сумму месячного платежа по кредиту: "))
utilities_debt = float(input("Введите задолженность за комуннальные услуги: "))

remaining_amout = salary - credit_paument - utilities_debt

print(f"Сумма, которая останется после всех выплат: {remaining_amout}")