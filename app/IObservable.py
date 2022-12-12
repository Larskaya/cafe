import abc
from app.IObserver import IObserver


class IObservable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_observer(self, o: IObserver):
        pass

    @abc.abstractmethod
    def remove_observer(self, o: IObserver):
        pass

    @abc.abstractmethod
    def notify(self):
        pass
