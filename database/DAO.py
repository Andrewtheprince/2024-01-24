from database.DB_connect import DBConnect

class DAO:

    @staticmethod
    def getMethods():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ """
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result