import psycopg2


class Baker:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def add_baker(self, x):
        try:
            self.__cur.execute("insert into bakers (name) values (%s, )", (x))
            self.__db.commit()
        except psycopg2.Error as error:
            print('error adding' + str(error))
            return False
        return True

