from models.BadMachine import BadMachine

# from models.Machine import Machine
# from models.EliteMachine import EliteMachine

from models.Oven import Oven
from models.Fridge import Fridge
from models.ReadinessPanel import ReadinessPanel

from models.Baker import Baker
from models.Pie import Pie

from models.Visitor import Visitor

from data.recipes import recipes
from data.actions import actions

bad_machine = BadMachine(recipes, actions)
readiness_panel = ReadinessPanel()
oven = Oven()
baker = Baker(oven)

fridge = Fridge()


def make_drink(drink):
    bad_machine.make_coffee(drink)
    readiness_panel.add_product(drink)


def make_food(food):
    oven.bake(food.timer, food)
    ready_products = baker.work(oven)
    if ready_products:
        readiness_panel.add_product(food)


def make_order(visitor_name, wish) -> str:
    if wish.need_bake:
        make_food(wish)
        fridge.remove_product(wish)
    print('tablo', readiness_panel.show_products())
    return f'order for {visitor_name} received'


def main():
    pie1 = Pie(True, 10)
    pie2 = Pie(True, 10)
    pie3 = Pie(True, 10)
    pie4 = Pie(False, 2)

    fridge.add_product(pie1)
    fridge.add_product(pie2)
    fridge.add_product(pie3)
    fridge.add_product(pie4)

    v = Visitor('Tom')
    wish = v.choose_order([pie1, pie2, pie3, pie4])
    print(make_order(v.name, wish))

    print(fridge.check())


if __name__ == '__main__':
    main()
