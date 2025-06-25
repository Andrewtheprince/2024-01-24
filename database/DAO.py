from database.DB_connect import DBConnect
from model.method import Method

class DAO:

    @staticmethod
    def getMethods():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ select *
                    from go_methods"""
        cursor.execute(query)
        for row in cursor:
            result.append(Method(**row))
        cursor.close()
        conn.close()
        return result