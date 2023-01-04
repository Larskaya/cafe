from __main__ import app
from database.app import *

from flask import jsonify


@app.route('/api/game/fridge', methods=['GET'])
def get_products_f():
    products = get_products_from_fridge()
    result = []
    if products:
        for product in products:
            result.append({'name': product[3]})
        return jsonify({'products': result})
    return jsonify({'success': False})


@app.route('/api/game/warehouse', methods=['GET'])
def get_products_w():
    products = get_products_from_warehouse()
    result = []
    if products:
        for product in products:
            result.append({'name': product[3]})
        return jsonify({'products': result})
    return jsonify({'success': False})