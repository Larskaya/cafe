import sys

sys.path.append('../')

from main import application, connect_db


def create_db():
    db = connect_db()
    with application.open_resource('utils/create_tables.sql', mode='r') as f:
        db.cursor().execute(f.read())
    db.commit()
    db.close()
