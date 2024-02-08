import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str) -> None:
        with open(source_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish_name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                existing_dish = next(
                    (d for d in self.dishes if d.name == dish_name), None
                )

                if not existing_dish:
                    new_dish = Dish(dish_name, price)
                    existing_dish = new_dish
                    self.dishes.add(new_dish)

                existing_ingredient = next(
                    (i for i in self.ingredients if i.name == ingredient_name),
                    None,
                )

                if not existing_ingredient:
                    new_ingredient = Ingredient(ingredient_name)
                    existing_ingredient = new_ingredient
                    self.ingredients.add(new_ingredient)

                existing_dish.add_ingredient_dependency(
                    existing_ingredient, recipe_amount
                )
