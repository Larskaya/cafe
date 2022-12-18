from flask import request, jsonify, render_template
from __main__ import app

from database.app import add_baker


@app.route('/admin/baker', methods=['GET'])
def baker():
    return render_template('admin_panel/baker.html')


@app.route('/admin/baker/add', methods=['POST'])
def add():
    name = request.form['name']
    print(name)
    res = add_baker(name)
    if res:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})


@app.route('/admin/baker/change', methods=['PUT'])
def change_baker():
    pass


@app.route('/admin/baker/delete', methods=['DELETE'])
def delete_baker():
    pass
