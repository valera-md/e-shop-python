import psycopg2
from Money import Money
from Model import Model

#CRUD - DONE

class Product(Model):
    
    def __init__(self, id, name, price_id):
        Model.__init__(self, id)
        self.name = name
        self.price_id = price_id

# HWl:
# - add this method
# - find all products
# - return a list of product objects
    
    def findAll():
        sql = f"""
        SELECT * FROM "products";
        """
        products =[]
        results = Product.connectAndExecute(sql, True) # we need the result
        for result in results:
            p = Product(result[0], result[1], result[2])
            m = Money.find(result[2])
            p.price = m
            products.append(p)
        return products
    # HM1: refactor this function
    def findAllByPriceRange(min_price, max_price):
        sql = f"""
        SELECT * FROM "products" JOIN "money"
        ON "products".price_id = "money".id
        WHERE amount >= {min_price} AND amount <= {max_price};
        """
        products =[]
        results = Product.connectAndExecute(sql, True)
        for result in results:
            p = Product(result[0], result[1], result[2])
            m = Money.find(result[2])
            p.price = m
            products.append(p)
        return products
    # HM2: refactor this function
    def findAllByName(keyword):
        #sql = f"""
        #SELECT * FROM "products" JOIN "money"
        #N "products".price_id = "money".id
        #WHERE name LIKE '%{keyword}%';
        #"""
        sql = f"""
        SELECT * FROM "products"
        WHERE name LIKE '%{keyword}%';
        """
        products = []
        results = Product.connectAndExecute(sql, True)
        for result in results:
            p = Product(result[0], result[1], result[2])
            m = Money.find(result[2])
            p.price = m
            products.append(p)
        return products

    def find(id):
        sql = f"""
        SELECT * FROM "products" WHERE id = {id};
        """
        result = Product.connectAndExecute(sql, True)[0]
        #p = Product(result[0], result[1], result[2])
        # result len -> 3
        #p = Product(*result[:3])
        p = Product(*result)
        m = Money.find(result[2])
        p.price = m
        return p

    def save(self):
        sql = f"""
        BEGIN;
        INSERT INTO "products" VALUES({self.id}, '{self.name}', {self.price_id});
        COMMIT;
        """
        Product.connectAndExecute(sql)

    def delete(self):
        sql = f"""
        BEGIN;
        DELETE FROM "products" WHERE id = {self.id};
        COMMIT;
        """
        Product.connectAndExecute(sql)

    def update(self):
        sql = f"""
        BEGIN;
        UPDATE "products" SET name = '{self.name}' WHERE id = {self.id};
        COMMIT;
        """
        Product.connectAndExecute(sql)

# HW2:
# create in this class methods: delete(), update(), find()
        
    def __str__(self):
        #return f"Product <{self.id}, {self.name}, {self.price_id}, {self.price}>"
        return f"Product <{self.id:5}, {self.name:20}, {self.price_id:5}, {self.price}>"
    
    def __repr__(self):
        return self.__str__()
    
#SELECT * FROM "products" WHERE name = 'Product 10';
#SELECT * FROM "products" WHERE name LIKE 'Prod%';