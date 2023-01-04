from flask import request, jsonify, render_template
from __main__ import app
from database.Recipe import RecipeDB


@app.route('/admin/recipe', methods=['GET'])
def recipe():
    return render_template('admin_panel/recipe.html')