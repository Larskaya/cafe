from flask import g

from database.baker import BakerDB
from utils.connect import get_db


def add_baker(name):
    print(get_db())
    g.baker = BakerDB(get_db())
    if g.baker.add_baker(name):
        return True
    return False
