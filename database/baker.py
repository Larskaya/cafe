import psycopg2


class Baker:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def add_baker(self, name):
        try:
            self.__cur.execute("INSERT INTO bakers (name) VALUES (%s, )", (name, ))
            self.__db.commit()
        except psycopg2.Error as error:
            print('error adding' + str(error))
            return False
        return True

    def delete_baker(self, name):
        try:
            self.__cur.execute("DELETE FROM bakers WHERE id=(%s)", (name, ))
            self.__db.commit()
            if self.__cur.rowcount == 0:
                print('user not found')
                return False
        except psycopg2.Error as error:
            print('error deleting ' + str(error))
            return False
        return True

    def get_baker(self, name):
        try:
            self.__cur.execute(f"SELECT * FROM bakers WHERE name='{name}'")
            baker = self.__cur.fetchone()
            if baker:
                return baker
            return []
        except psycopg2.Error as error:
            print('error reading from db ' + str(error))
        return []
