## Superclass
# Inheritance, практичное применение наследования
# Model
# + id
# + connection
# |       |
# v       v
# Product Money
import psycopg2

class Model:
    def __init__(self, id):
        self.id = id

    def connectAndExecute(sql, returns = False):
        conn = psycopg2.connect("dbname=e-shop-python user=postgres password=1234")
        cursor = conn.cursor()
        cursor.execute(sql)
        
        if returns:
            results = cursor.fetchall()
            return results 