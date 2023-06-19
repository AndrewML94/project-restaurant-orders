from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    name = "bacon"
    exp_restrictions = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    ingredient = Ingredient(name)
    assert ingredient.name == name
    assert ingredient.restrictions == exp_restrictions

    expected_repr = f"Ingredient('{name}')"
    assert repr(ingredient) == expected_repr

    same_ingredient = Ingredient(name)
    assert ingredient == same_ingredient

    different_ingredient = Ingredient("manteiga")
    assert ingredient != different_ingredient

    assert hash(ingredient) == hash(same_ingredient)
    assert hash(ingredient) != hash(different_ingredient)

    unknown_ingredient = Ingredient("tomate")
    assert unknown_ingredient.restrictions == set()

    expected_repr_unknown = "Ingredient('tomate')"
    assert repr(unknown_ingredient) == expected_repr_unknown

    assert unknown_ingredient != ingredient
    assert unknown_ingredient != different_ingredient

    assert hash(unknown_ingredient) != hash(ingredient)
    assert hash(unknown_ingredient) != hash(different_ingredient)
