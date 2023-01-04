from flask import g

from database.Baker import BakerDB
from database.Storage import StorageDB
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


def get_products_from_fridge():
    g.storage = StorageDB(get_db())
    products = g.storage.get_products(1)
    if products:
        return products
    return []


def get_products_from_warehouse():
    g.storage = StorageDB(get_db())
    products = g.storage.get_products(2)
    if products:
        return products
    return []










