from models.Fridge import Fridge

fridge = Fridge()


def test_adding_product():
    products = fridge.products_amount
    fridge.add_product('pie')
    assert fridge.products_amount == products + 1


def test_removing_product():
    products = fridge.products_amount
    fridge.remove_product('pie')
    assert fridge.products_amount == products - 1
