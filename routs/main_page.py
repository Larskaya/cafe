from flask import render_template
from __main__ import app


@app.route('/', methods=['GET'])
def get():
    context = {'word': 'cat'}
    return render_template('main_page.html', context=context)
