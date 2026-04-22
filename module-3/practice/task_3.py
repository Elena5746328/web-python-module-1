prices = { "bread": 20, "milk": 80, "cheese": 25}
cart = {"bread": 2, "cola": 1, "milk": 3}
cost = 0

for item, quantity in cart.items():
    if item not in prices:
        print(f"Товар '{item}' отсутствует в прайс-листе")
    else:
        cost += prices[item] * quantity

print(f"Итоговая стоимость корзины: {cost} рублей")
