from flask import render_template
from __main__ import app


@app.route('/', methods=['GET'])
def get():
    return render_template('main_page.html')
