class Visitor:
    def __init__(self, name):
        self.name = name
        self.drink = None
        self.food = None
        self.order_received = False

    def choose_order(self, food_list):
        return food_list[2]

    def get_order(self):
        self.order_received = True
