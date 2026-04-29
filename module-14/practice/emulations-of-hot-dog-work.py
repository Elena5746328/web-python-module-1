from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    key: str
    price: float
    cost: float

@dataclass
class Recipe:
    name: str
    Ingredient_keys: list[str]

class RecipeFactory:
    def get_standart_recipes() -> dict[int, Recipe]:
        return {
            0: Recipe("Хот-дог-1", ["hot dog bun", "sausage", "ketchup", "mustard"]),
            1: Recipe("Хот-дог-2", ["hot dog bun", "sausage", "mayonnaise", "sweet onion"]),
            2: Recipe("Хот-дог-2", ["hot dog bun", "sausage", "mustard", "pickle"])
        }
    
class HotDogBilder:
    def __init__(self):
        self._ingredient = ["hot dog bun", "sausage"]