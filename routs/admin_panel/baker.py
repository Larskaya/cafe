from flask import render_template
from __main__ import app


@app.route('/admin/baker/add', methods=['POST'])
def add_baker():
    pass


@app.route('/admin/baker/change', methods=['PUT'])
def change_baker():
    pass


@app.route('/admin/baker/delete', methods=['DELETE'])
def delete_baker():
    pass
