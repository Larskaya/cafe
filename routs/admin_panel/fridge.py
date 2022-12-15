from flask import render_template
from __main__ import app


@app.route('/admin/fridge/add', methods=['POST'])
def add_fridge():
    pass


@app.route('/admin/fridge/change', methods=['PUT'])
def change_fridge():
    pass


@app.route('/admin/fridge/delete', methods=['DELETE'])
def delete_fridge():
    pass


