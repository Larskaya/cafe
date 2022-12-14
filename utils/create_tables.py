import sys

from connect import connect_db
sys.path.append('../')
from main import app


def create_tables():
    db = connect_db()
    with app.open_resource('utils/create_tables.sql', mode='r') as f:
        db.cursor().execute(f.read())
    db.commit()
    db.close()


create_tables()
