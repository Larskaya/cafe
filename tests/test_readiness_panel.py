from models.ReadinessPanel import ReadinessPanel

readinessPanel = ReadinessPanel()


def test_show_products():
    products_amount = len(readinessPanel.show_products())
    assert 3 >= products_amount >= 0
