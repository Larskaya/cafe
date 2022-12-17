import os
from flask import Flask

from models.BadMachine import BadMachine
from models.Oven import Oven
from models.Fridge import Fridge
from models.ReadinessPanel import ReadinessPanel
from models.Baker import Baker
from models.Pie import Pie
from models.Visitor import Visitor

from data.recipes import recipes
from data.actions import actions


app = Flask(__name__, static_url_path='')

app.config['SECRET_KEY'] = '5k2G7&eqZo$e8eYIb9'
app.config.from_object(__name__)

DATABASE = '/tmp/cafe.db'
DEBUG = True
SECRET_KEY = 'T4gU@8Vc7&v^E27oOru'

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'cafe.db')))

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


from routs.admin_panel import admin, baker, storage, oven, product, recipe
from routs import main_page


if __name__ == '__main__':
    # main()
    app.run(host='0.0.0.0', port=5555, debug=True)
