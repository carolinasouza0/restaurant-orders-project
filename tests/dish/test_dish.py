from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest

# Req 2


def test_dish():
    dish = Dish("Lasanha", 20.0)
    assert dish.name == "Lasanha"
    assert dish.price == 20.0
    eq_dish = Dish("Lasanha", 20.0)
    assert hash(dish) == hash(eq_dish)
    assert dish == eq_dish

    neq_dish = Dish("Ravioli", 20.0)
    assert hash(dish) != hash(neq_dish)
    assert dish != neq_dish

    repr_dish = "Dish('Lasanha', R$20.00)"
    assert repr(dish) == repr_dish

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Lasanha", "000")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Lasanha", 0.0)

    dish.add_ingredient_dependency(Ingredient("massa de lasanha"), 1)
    dish.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)
    assert dish.get_ingredients() == {
        Ingredient("massa de lasanha"),
        Ingredient("queijo mussarela"),
    }

    assert dish.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
        Restriction.ANIMAL_DERIVED,
    }
