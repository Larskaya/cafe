import psycopg2


class StorageDB:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def add_storage(self, name):
        try:
            self.__cur.execute("INSERT INTO storages (name) VALUES (%s, )", (name, ))
            self.__db.commit()
        except psycopg2.Error as error:
            print('error adding' + str(error))
            return False
        return True

    def get_products(self, designation):
        try:
            self.__cur.execute(f"SELECT * "
                               f"FROM products_in_storages as ps "
                               f"INNER JOIN products "
                               f"ON ps.product_id = products.id "
                               f"WHERE storage_id = {designation} ")
            products = self.__cur.fetchall()
            print('products: ', products)
            if products:
                return products
        except psycopg2.Error as error:
            print('error reading from db ' + str(error))
        return []








