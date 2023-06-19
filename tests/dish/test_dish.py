import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient


def test_dish():
    dish = Dish("Spaghetti Carbonara", 15.99)
    assert dish.name == "Spaghetti Carbonara"
    assert dish.price == 15.99
    assert dish.recipe == {}

    assert repr(dish) == "Dish('Spaghetti Carbonara', R$15.99)"

    dish1 = Dish("Spaghetti Carbonara", 15.99)
    dish2 = Dish("Spaghetti Carbonara", 15.99)
    dish3 = Dish("Lasagna", 20.99)
    assert dish1 == dish2
    assert dish1 != dish3
    assert dish2 != dish3

    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)
    assert hash(dish2) != hash(dish3)

    ingredient1 = Ingredient("Pasta")
    ingredient2 = Ingredient("Bacon")
    dish.add_ingredient_dependency(ingredient1, 200)
    dish.add_ingredient_dependency(ingredient2, 100)

    ingredient3 = Ingredient("Cheese")
    dish.add_ingredient_dependency(ingredient3, 150)
    restrictions = dish.get_restrictions()
    expected_restrictions = {"ANIMAL_DERIVED", "ANIMAL_MEAT"}
    assert restrictions.issubset(expected_restrictions)

    ingredients = dish.get_ingredients()
    expected_ingredients = {ingredient1, ingredient2, ingredient3}
    assert ingredients == expected_ingredients

    with pytest.raises(TypeError):
        Dish("Spaghetti Carbonara", "15.99")

    with pytest.raises(ValueError):
        Dish("Spaghetti Carbonara", -10.99)
