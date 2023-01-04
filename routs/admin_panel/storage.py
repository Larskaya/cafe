from flask import render_template
from __main__ import app
from database.Storage import StorageDB


@app.route('/admin/storage', methods=['GET'])
def storage():
    return render_template('admin_panel/storage.html')


@app.route('/admin/storage/add', methods=['POST'])
def add_fridge():
    pass


@app.route('/admin/storage/change', methods=['PUT'])
def change_fridge():
    pass


@app.route('/admin/storage/delete', methods=['DELETE'])
def delete_fridge():
    pass


