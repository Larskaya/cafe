import flask
import psycopg2


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
        print('connection error -', str(e))
    return conn


def get_db():
    print('get db', flask.g)
    """ connect to database """
    if not hasattr(flask.g, 'link_db'):
        flask.g.link_db = connect_db()
    return flask.g.link_db
