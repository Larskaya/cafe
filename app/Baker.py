import time

from app.Pie import Pie


class Baker:
    def __init__(self) -> None:
        self.is_working = False

    def work(self, oven) -> list[Pie]:
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
