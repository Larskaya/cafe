from flask import request, jsonify, render_template
from __main__ import app


@app.route('/admin/baker/add', methods=['POST'])
def add_baker():
    form_data = request.form
    res = Baker.add_baker(form_data[name])
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
