from app.BadMachine import BadMachine

from app.Machine import Machine
from app.EliteMachine import EliteMachine

from app.Oven import Oven
from app.Fridge import Fridge
from app.ReadinessPanel import ReadinessPanel

from app.Baker import Baker
from app.Pie import Pie

from app.Visitor import Visitor

from data.recipes import recipes
from data.actions import actions

bad_machine = BadMachine(recipes, actions)
readiness_panel = ReadinessPanel()
baker = Baker()
oven = Oven()
fridge = Fridge()


def make_drink(drink):
    bad_machine.make_coffee(drink)
    readiness_panel.add_product(drink)


def make_food(food):
    oven.bake(food.timer, food)
    ready_products = baker.work(oven)
    if ready_products:
        readiness_panel.add_product(food)


def make_order(visitor_name, wish):
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
    make_order(v.name, wish)

    print(fridge.check())


if __name__ == '__main__':
    main()
