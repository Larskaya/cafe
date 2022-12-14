from flask import render_template
from __main__ import app

from database.Product import ProductDB


@app.route('/admin/product', methods=['GET'])
def product():
    return render_template('admin_panel/product.html')


@app.route('/admin/product/add', methods=['POST'])
def add_product():
    pass


@app.route('/admin/product/change', methods=['PUT'])
def change_product():
    pass


@app.route('/admin/product/delete', methods=['DELETE'])
def delete_product():
    pass

