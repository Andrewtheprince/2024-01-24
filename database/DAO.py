from database.DB_connect import DBConnect
from model.method import Method
from model.product import Product

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

    @staticmethod
    def getNodi(anno, metodo):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ select gp.*, sum(gds.Quantity*gds.Unit_sale_price) as VenditaTot
                    from go_products gp, go_daily_sales gds
                    where gds.Order_method_code = %s and YEAR(gds.Date) = %s and gp.Product_number = gds.Product_number
                    group by gp.Product_number"""
        cursor.execute(query, (metodo, anno, ))
        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result