import psycopg2
from Model import Model
from Bag import Bag
from Product import Product

class BagItem(Model):
    
    def __init__(self, id, bag_id, product_id, quantity):
        Model.__init__(self, id)
        self.bag_id = bag_id
        self.product_id = product_id
        self.quantity = quantity

    def find(id):
        sql = f"""
        SELECT * FROM "bag_items" WHERE id = {id};
        """
        result = BagItem.connectAndExecute(sql, True)[0]
        bi = BagItem(*result)
        b = Bag.find(bi.bag_id)
        p = Product.find(bi.product_id)
        bi.bag = b
        bi.product = p
        return bi

    def findAllByBag(bag_id):
        sql = f"""
        SELECT * FROM "bag_items" WHERE bag_id = {bag_id};
        """
        items =[]
        results = BagItem.connectAndExecute(sql, True) # we need the result
        for result in results:
            bi = BagItem(*result)
            b = Bag.find(bi.bag_id)
            p = Product.find(bi.product_id)
            bi.bag = b
            bi.product = p
            items.append(bi)
        return items

    def save(self):
        sql = f"""
        BEGIN;
        INSERT INTO "bag_items" VALUES({self.id}, {self.bag_id}, '{self.product_id}', {self.quantity});
        COMMIT;
        """
        BagItem.connectAndExecute(sql)

    def delete(self):
        sql = f"""
        BEGIN;
        DELETE FROM "bag_items" WHERE id = {self.id};
        COMMIT;
        """
        BagItem.connectAndExecute(sql)

    def update(self):
        sql = f"""
        BEGIN;
        UPDATE "bag_items" SET bag_id = {self.bag_id}, product_id = '{self.product_id}', quantity = {self.quantity} WHERE id = {self.id};
        COMMIT;
        """
        BagItem.connectAndExecute(sql)

    def __str__(self):
        return f"BagItem <{self.id}, {self.bag_id}, {self.product_id}, {self.quantity}, {self.bag}, {self.product}>"
        #return f"BagItem <{self.id}, {self.bag_id}, {self.product_id}, {self.quantity}>"
