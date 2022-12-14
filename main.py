import flask
import os
import psycopg2
from flask import Flask
#
# import sys
# import importlib

# from app import main
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# sys.path.insert(0, BASE_DIR)
# importlib.reload(main)


application = Flask(__name__, static_url_path='')

application.config['SECRET_KEY'] = '5k2G7&eqZo$e8eYIb9'
application.config.from_object(__name__)

DATABASE = '/tmp/cafe.db'
DEBUG = True
SECRET_KEY = 'T4gU@8Vc7&v^E27oOru'

application.config.update(dict(DATABASE=os.path.join(application.root_path, 'cafe.db')))


def connect_db():
    conn = False
    try:
        conn = psycopg2.connect(
            database='cafe',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432'
        )
    except Exception as e:
        print('connection error', str(e))
    return conn


def get_db():
    print('get db', flask.g)
    """ connect to database """
    if not hasattr(flask.g, 'link_db'):
        flask.g.link_db = connect_db()
    return flask.g.link_db


from routs import main_page


if __name__ == '__main__':
    # main()
    application.run(host='0.0.0.0', debug=True)
