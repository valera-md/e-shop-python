import psycopg2
from Product import Product
from Model import Model

class Stock(Model):
    
    def __init__(self, id, product_id, quantity):
        Model.__init__(self, id)
        self.product_id = product_id
        self.quantity = quantity

# HWl:
# - add this method
# - find all products
# - return a list of product objects
    
    def findAll():
        sql = f"""
        SELECT * FROM "stock";
        """
        products_in_stock = []
        results = Stock.connectAndExecute(sql, True) # we need the result
        for result in results:
            s = Stock(result[0], result[1], result[2])
            p = Product.find(result[1])
            s.product_description = p
            products_in_stock.append(s)
        return products_in_stock

    def findAllByName(keyword):
        sql = f"""
        SELECT * FROM "stock" JOIN "products"
        ON "stock".product_id = "products".id
        WHERE name LIKE '%{keyword}%';
        """
        products_in_stock = []
        results = Stock.connectAndExecute(sql, True)
        for result in results:
            s = Stock(result[0], result[1], result[2])
            p = Product.find(result[1])
            s.product_description = p
            products_in_stock.append(s)
        return products_in_stock

    def find(id):
        sql = f"""
        SELECT * FROM "stock" WHERE id = {id};
        """
        result = Stock.connectAndExecute(sql, True)[0]
        #s = Stock(result[0], result[1], result[2])
        # result len -> 3
        #s = Stock(*result[:3])
        s = Stock(*result)
        p = Product.find(result[1])
        s.product_description = p
        return s

    def save(self):
        sql = f"""
        BEGIN;
        INSERT INTO "stock" VALUES({self.id}, '{self.product_id}', {self.quantity});
        COMMIT;
        """
        Stock.connectAndExecute(sql)

    def delete(self):
        sql = f"""
        BEGIN;
        DELETE FROM "stock" WHERE id = {self.id};
        COMMIT;
        """
        Stock.connectAndExecute(sql)

    def update(self):
        sql = f"""
        BEGIN;
        UPDATE "stock" SET quantity = '{self.quantity}' WHERE id = {self.id};
        COMMIT;
        """
        Stock.connectAndExecute(sql)
        
    def __str__(self):
        return f"Stock <{self.id}, {self.product_id}, {self.quantity}, {self.product_description}>"
    
    def __repr__(self):
        return self.__str__()