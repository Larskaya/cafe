from datetime import datetime
from typing import List

from models.Pie import Pie
from models.IObserver import IObserver
from models.IObservable import IObservable


class Oven(IObservable):
    def __init__(self) -> None:
        self.enabled = False
        self.work_time = 0
        self.seconds = 0
        self.start_time = None
        self.products = []
        self.__observers: List[IObserver] = []

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

    def add_observer(self, observer: IObserver):
        self.__observers.append(observer)

    def remove_observer(self, observer: IObserver):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update(self.enabled)
