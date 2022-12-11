from datetime import datetime
from app.Pie import Pie


class Oven:
    def __init__(self) -> None:
        self.enabled = False
        self.work_time = 0
        self.seconds = 0
        self.start_time = None
        self.products = []

    def bake(self, seconds, product):
        self.seconds = seconds
        self.products.append(product)
        self.enabled = True
        self.start_time = datetime.now()

    def get_status(self) -> int:
        time = datetime.now()
        difference = time - self.start_time
        remaining_time = self.seconds - difference.seconds
        if remaining_time <= 0:
            for product in self.products:
                product.set_ready()
        return remaining_time

    def stop(self) -> list[Pie]:
        self.enabled = False
        ready_products = self.products
        self.products = []
        return ready_products
