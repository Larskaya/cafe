from flask import render_template
from __main__ import app


@app.route('/admin', methods=['GET'])
def get_panel():
    return render_template('admin_panel.html')
