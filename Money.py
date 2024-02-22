import psycopg2
from Model import Model
#CRUD - DONE

class Money(Model):
    
    def __init__(self, id, amount, currency):
        Model.__init__(self, id) # delegating constructor, делегировать конструктор
        self.amount = amount
        self.currency = currency

    def find(id):
        sql = f"""
        SELECT * FROM "money" WHERE id = {id};
        """
        result = Money.connectAndExecute(sql, True)[0]
        m = Money(*result)
        return m

    def save(self):
        sql = f"""
        BEGIN;
        INSERT INTO "money" VALUES({self.id}, {self.amount}, '{self.currency}');
        COMMIT;
        """
        Money.connectAndExecute(sql)

    def delete(self):
        sql = f"""
        BEGIN;
        DELETE FROM "money" WHERE id = {self.id};
        COMMIT;
        """
        Money.connectAndExecute(sql)

    def update(self):
        sql = f"""
        BEGIN;
        UPDATE "money" SET amount = {self.amount}, currency = '{self.currency}' WHERE id = {self.id};
        COMMIT;
        """
        Money.connectAndExecute(sql)

    def __str__(self):
        #return f"Money <{self.id}, {self.amount}, {self.currency}>"
        return f"Money <{self.id:5}, {self.amount:8}, {self.currency}>"
