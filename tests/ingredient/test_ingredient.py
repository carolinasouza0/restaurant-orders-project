from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingredient = Ingredient("queijo mussarela")
    assert ingredient.name == "queijo mussarela"
    assert ingredient.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
    }

    ingredient = Ingredient("bacon")
    assert repr(ingredient) == "Ingredient('bacon')"

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    assert ingredient1 == ingredient2

    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("farinha")
    assert hash(ingredient1) == hash(ingredient2)

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("bacon")
    assert hash(ingredient1) != hash(ingredient2)

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("bacon")
    assert not ingredient1 == ingredient2

    ingredient = Ingredient("farinha")
    assert repr(ingredient) == "Ingredient('farinha')"

    ingredient = Ingredient("farinha")
    assert ingredient.name == "farinha"

    ingredient = Ingredient("farinha")
    assert ingredient.restrictions == {Restriction.GLUTEN}

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    assert ingredient1 == ingredient2
