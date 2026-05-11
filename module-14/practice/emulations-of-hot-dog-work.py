from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List, Dict

@dataclass
class Ingredient:
    name: str
    key: str
    price: float
    cost: float
    
@dataclass
class Recipe:
    name: str
    ingredient_keys: List[str]

class RecipeFactory:
    @staticmethod
    def get_standard_recipes() -> Dict[int, Recipe]:
        return {
            0: Recipe("Классический хот-дог", ["hot dog bun", "sausage", "ketchup", "mustard"]),
            1: Recipe("Хот-дог с луком", ["hot dog bun", "sausage", "mayonnaise", "sweet onion"]),
            2: Recipe("Острый хот-дог", ["hot dog bun", "sausage", "mustard", "pickle", "jalapeno"])
        }

class HotDogBuilder:
    def __init__(self):
        self._ingredient_keys = ["hot dog bun", "sausage"]

    def add_ingredient(self, key: str):
        if key not in self._ingredient_keys:
            self._ingredient_keys.append(key)
        return self

    def build(self):
        return Recipe("Пользовательский хот-дог", self._ingredient_keys)

@dataclass
class OrderItem:
    recipe: Recipe
    quantity: int

    def total_price(self, ingredients: Dict[str, Ingredient]) -> float:
        one_hotdog_price = sum(ingredients[key].price for key in self.recipe.ingredient_keys)
        return one_hotdog_price * self.quantity

    def total_cost(self, ingredients: Dict[str, Ingredient]) -> float:
        one_hotdog_cost = sum(ingredients[key].cost for key in self.recipe.ingredient_keys)
        return one_hotdog_cost * self.quantity

@dataclass
class Order:
    items: List[OrderItem]
    payment_type: str

    def total_price(self, ingredients: Dict[str, Ingredient]):
        subtotal = sum(item.total_price(ingredients) for item in self.items)
        total_quantity = sum(item.quantity for item in self.items)
        if total_quantity >= 5:
            discount = 0.15
        elif total_quantity >= 3:
            discount = 0.10
        else:
            discount = 0
        return subtotal * (1 - discount)


    def total_cost(self, ingredients: Dict[str, Ingredient]):
        return sum(item.total_cost(ingredients) for item in self.items)

    def total_profit(self, ingredients: Dict[str, Ingredient]):
        return self.total_price(ingredients) - self.total_cost(ingredients)

    def to_text(self, ingredients: Dict[str, Ingredient]) -> str:
        lines = ["Информация о заказе:"]
        total_quantity = 0

        for item in self.items:
            total_quantity += item.quantity
            ingredient_names = [ingredients[key].name for key in item.recipe.ingredient_keys]
            lines.append(f"Хот-дог: {item.recipe.name}")
            lines.append(f"Количество: {item.quantity}")
            lines.append("Состав:")
            for name in ingredient_names:
                lines.append(f"- {name}")
            lines.append(f"Цена позиции: {item.total_price(ingredients)} руб.")
            lines.append("")

        lines.append(f"Общее количество: {total_quantity} шт.")
        lines.append(f"Способ оплаты: {self.payment_type}")
        lines.append(f"Итого к оплате: {self.total_price(ingredients)} руб.")

        return "\n".join(lines)

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"Оплата наличными выполнена на сумму {amount} руб."


class CardPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"Оплата картой выполнена на сумму {amount} руб."

class FileOrderSaver:
    def __init__(self, filename: str = "hotdog_order.txt"):
        self.filename = filename

    def save(self, order: Order, ingredients: Dict[str, Ingredient]):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(order.to_text(ingredients))
            file.write("\n" + "-" * 50 + "\n")

def create_ingredients() -> Dict[str, Ingredient]:
    return {
        "hot dog bun": Ingredient("Булочка для хот-дога", "hot dog bun", 30.0, 15.0),
        "sausage": Ingredient("Сосиска", "sausage", 80.0, 40.0),
        "ketchup": Ingredient("Кетчуп", "ketchup", 15.0, 7.0),
        "mustard": Ingredient("Горчица", "mustard", 15.0, 7.0),
        "mayonnaise": Ingredient("Майонез", "mayonnaise", 15.0, 8.0),
        "sweet onion": Ingredient("Сладкий лук", "sweet onion", 20.0, 10.0),
        "pickle": Ingredient("Маринованный огурец", "pickle", 25.0, 12.0),
        "jalapeno": Ingredient("Халапеньо", "jalapeno", 30.0, 18.0)
    }

def create_stock() -> Dict[str, int]:
    return {
        "hot dog bun": 50,
        "sausage": 60,
        "ketchup": 30,
        "mustard": 25,
        "mayonnaise": 20,
        "sweet onion": 15,
        "pickle": 10,
        "jalapeno": 8
    }

def get_toppings() -> List[str]:
    return ["ketchup", "mustard", "mayonnaise", "sweet onion", "pickle", "jalapeno"]

def create_custom_recipe(inventory: 'Inventory') -> Recipe:
    builder = HotDogBuilder()
    print("Создание пользовательского хот-дога")

    for key in get_toppings():
        ingredient = inventory.ingredients[key]
        choice = input(f"Хотите добавить {ingredient.name}? (да/нет): ").lower()
        if choice == "да":
            builder.add_ingredient(ingredient.key)

    return builder.build()

class Inventory:
    def __init__(self, ingredients: Dict[str, Ingredient], stock: Dict[str, int]):
        self.ingredients = ingredients
        self.stock = stock

    def has_enough(self, ingredient_keys: List[str], quantity: int) -> bool:
        for key in ingredient_keys:
            if self.stock.get(key, 0) < quantity:
                return False
        return True

    def reduce_stock(self, ingredient_keys: List[str], quantity: int):
        for key in ingredient_keys:
            self.stock[key] -= quantity

    def show(self):
        print("\nНаличие ингредиентов:")
        print("-" * 30)
        low_items = []
        for key, count in self.stock.items():
            ingredient = self.ingredients[key]
            status = " [НИЗКИЙ ЗАПАС]" if count <= 5 else ""
            print(f"{ingredient.name}: {count} шт.{status}")
            if count <= 5:
                low_items.append(ingredient.name)
        if low_items:
            print("\nВНИМАНИЕ! Требуется пополнение:")
            for item in low_items:
                print(f"- {item}")

class SalesReport:
    def __init__(self):
        self.profit = 0.0
        self.revenue = 0.0
        self.sold_count = 0

    def add_order(self, order: Order, ingredients: Dict[str, Ingredient]):
        self.sold_count += sum(item.quantity for item in order.items)
        self.revenue += order.total_price(ingredients)
        self.profit += order.total_profit(ingredients)

    def show(self):
        print("\n" + "=" * 40)
        print("ОТЧЁТ О ПРОДАЖАХ")
        print("=" * 40)
        print(f"Продано хот-догов: {self.sold_count} шт.")
        print(f"Общая выручка: {self.revenue} руб.")
        print(f"Общая прибыль: {self.profit} руб.")
        print("=" * 40)

def show_menu():
    print("\n" + "=" * 50)
    print("КИОСК ПО ПРОДАЖЕ ХОТ-ДОГОВ")
    print("=" * 50)
    print("1. Создать заказ")
    print("2. Отчёт о продажах")
    print("3. Наличие ингредиентов")
    print("4. Выход")
    print("-" * 50)

def show_standard_recipes(recipes: Dict[int, Recipe], ingredients: Dict[str, Ingredient]):
    print("\nСтандартные хот-доги:")
    print("-" * 30)
    for number, recipe in recipes.items():
        recipe_price = sum(ingredients[key].price for key in recipe.ingredient_keys)
        print(f"{number + 1}. {recipe.name}")
        print(f"Состав: {', '.join(ingredients[key].name for key in recipe.ingredient_keys)}")
        print(f"Цена за штуку: {recipe_price} руб.")
        print()
    print("0. Создать свой хот-дог")

def choose_recipe(recipes: Dict[int, Recipe], ingredients: Dict[str, Ingredient], inventory: Inventory) -> Recipe:
    while True:
        show_standard_recipes(recipes, ingredients)
        choice = input("Выберите вариант (0–3): ")

        if choice == "0":
            return create_custom_recipe(inventory)
        elif choice in ["1", "2", "3"]:
            recipe = recipes[int(choice) - 1]
            if inventory.has_enough(recipe.ingredient_keys, 1):
                return recipe
            else:
                print("Извините, недостаточно ингредиентов для этого хот-дога!")
        else:
            print("Неверный выбор, попробуйте снова.")

def choose_payment() -> tuple[PaymentStrategy, str]:
    print("\nВыберите способ оплаты:")
    print("1 — Наличные")
    print("2 — Карта")

    while True:
        choice = input("Ваш выбор (1 или 2): ")
        if choice == "1":
            return CashPayment(), "Наличные"
        elif choice == "2":
            return CardPayment(), "Карта"
        else:
            print("Пожалуйста, выберите 1 или 2.")

def create_order(
    ingredients: Dict[str, Ingredient],
    inventory: Inventory,
    report: SalesReport,
    file_saver: FileOrderSaver
):
    recipes = RecipeFactory.get_standard_recipes()
    items: List[OrderItem] = []

    print("\nНАЧАЛО ОФОРМЛЕНИЯ ЗАКАЗА")
    while True:
        recipe = choose_recipe(recipes, ingredients, inventory)
        quantity = int(input("Введите количество: "))

        if not inventory.has_enough(recipe.ingredient_keys, quantity):
            print("Недостаточно ингредиентов для выполнения заказа.")
            continue

        items.append(OrderItem(recipe, quantity))
        more = input("Добавить ещё один вид хот-дога? (да/нет): ").lower()
        if more != "да":
            break

    payment_strategy, payment_type = choose_payment()
    order = Order(items, payment_type)

    for item in items:
        inventory.reduce_stock(item.recipe.ingredient_keys, item.quantity)

    amount = order.total_price(ingredients)

    print(payment_strategy.pay(amount))

    file_saver.save(order, ingredients)

    report.add_order(order, ingredients)
    print("Заказ успешно оформлен!")

def main():
    ingredients = create_ingredients()
    stock = create_stock()
    inventory = Inventory(ingredients, stock)
    report = SalesReport()
    file_saver = FileOrderSaver()

    while True:
        show_menu()
        choice = input("Выберите пункт меню (1–4): ")

        if choice == "1":
            create_order(ingredients, inventory, report, file_saver)
        elif choice == "2":
            report.show()
        elif choice == "3":
            inventory.show()
        elif choice == "4":
            print("Спасибо за работу с киоском! До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт от 1 до 4.")

main()


