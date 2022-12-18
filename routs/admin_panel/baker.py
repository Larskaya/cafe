from flask import request, jsonify, render_template
from __main__ import app

from database.app import add_baker, delete_baker, change_baker


@app.route('/admin/baker', methods=['GET'])
def baker():
    return render_template('admin_panel/baker.html')


@app.route('/admin/baker/add', methods=['POST'])
def add():
    name = request.form['name']
    if add_baker(name):
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})


@app.route('/admin/baker/change', methods=['POST'])
def change():
    name = request.form['name']
    new_name = request.form['newname']
    if change_baker(name, new_name):
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})


@app.route('/admin/baker/delete', methods=['DELETE'])
def delete():
    name = request.form['name']
    if delete_baker(name):
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})
