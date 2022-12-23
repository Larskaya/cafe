import time

from models.Product import Product
from models.IObserver import IObserver
from models.IObservable import IObservable


class Baker(IObserver):
    def __init__(self, obj: IObservable) -> None:
        self.is_working = False
        self.__oven = obj
        obj.add_observer(self)

    def work(self, oven) -> list[Product]:
        pies = None
        self.is_working = True
        while self.is_working:
            time.sleep(1)
            status = oven.get_status()
            print('status', status)
            if status <= 0:
                pies = oven.stop()
                self.stop()
                break
        return pies

    def stop(self):
        self.is_working = False

    def update(self, enabled: bool):
        if not enabled:
            print('process has been finished - oven is disable')
            self.__oven.remove_observer(self)
