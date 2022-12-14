class ReadinessPanel:
    def __init__(self) -> None:
        self.product_names = []

    def add_product(self, product):
        self.product_names.append(product)

    def show_products(self) -> list:
        return self.product_names[-3::]

    def delete_product(self, product):
        self.product_names.remove(product)
