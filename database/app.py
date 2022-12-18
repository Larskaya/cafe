from flask import g

from database.baker import BakerDB
from utils.connect import get_db


def add_baker(name):
    g.baker = BakerDB(get_db())
    if g.baker.add_baker(name):
        return True
    return False


def delete_baker(name):
    g.baker = BakerDB(get_db())
    if g.baker.delete_baker(name):
        return True
    return False


def change_baker(name, new_name):
    g.baker = BakerDB(get_db())
    if g.baker.change_baker(name, new_name):
        return True
    return False
