class Product:
    def __init__(self, need_bake, timer):
        self.is_ready = False
        self.need_bake = need_bake
        self.timer = timer

    def set_ready(self):
        self.is_ready = True

    def get_status(self) -> bool:
        return self.is_ready
