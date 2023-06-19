import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.menu(source_path)

    def menu(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            dish_dict = {}
            for row in reader:
                dish_name = row[0]
                price = float(row[1])
                ingredient_name = row[2]
                ingredient_quant = int(row[3])

                ingredient = Ingredient(ingredient_name)
                dish = dish_dict.get(dish_name)
                if not dish:
                    dish = Dish(dish_name, price)
                    dish_dict[dish_name] = dish
                    self.dishes.add(dish)
                dish.add_ingredient_dependency(ingredient, ingredient_quant)
