from flask import request, jsonify, render_template
from __main__ import app
from database.recipe import Recipe


@app.route('/admin/recipe', methods=['GET'])
def recipe():
    return render_template('admin_panel/recipe.html')