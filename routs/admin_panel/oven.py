from flask import render_template
from __main__ import app

from database.Oven import OvenDB


@app.route('/admin/oven', methods=['GET'])
def oven():
    return render_template('admin_panel/oven.html')


@app.route('/admin/oven/add', methods=['POST'])
def add_oven():
    pass


@app.route('/admin/oven/change', methods=['PUT'])
def change_oven():
    pass


@app.route('/admin/oven/delete', methods=['DELETE'])
def delete_oven():
    pass
