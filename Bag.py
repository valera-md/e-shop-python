import psycopg2
from Model import Model
from Money import Money
from Client import Client

class Bag(Model):
    
    def __init__(self, id, cost_id, client_id):
        Model.__init__(self, id) # delegating constructor, делегировать конструктор
        self.cost_id = cost_id
        self.client_id = client_id

    def find(id):
        sql = f"""
        SELECT * FROM "bags" WHERE id = {id};
        """
        result = Bag.connectAndExecute(sql, True)[0]
        b = Bag(*result)
        m = Money.find(b.cost_id)
        c = Client.find(b.client_id)
        b.cost = m
        b.client = c
        return b

    def findByClient(client_id):
        sql = f"""
        SELECT * FROM "bags" WHERE client_id = {client_id};
        """
        results = Bag.connectAndExecute(sql, True)
        if len(results) > 0:
            result = results[0]
            b = Bag(*result)
            m = Money.find(b.cost_id)
            c = Client.find(b.client_id)
            b.cost = m
            b.client = c
            return b
        else:
            return None

    def save(self):
        sql = f"""
        BEGIN;
        INSERT INTO "bags" VALUES({self.id}, {self.cost_id}, '{self.client_id}');
        COMMIT;
        """
        Bag.connectAndExecute(sql)

    def delete(self):
        sql = f"""
        BEGIN;
        DELETE FROM "bags" WHERE id = {self.id};
        COMMIT;
        """
        Bag.connectAndExecute(sql)

    def update(self):
        sql = f"""
        BEGIN;
        UPDATE "bags" SET cost_id = {self.cost_id}, client_id = '{self.client_id}' WHERE id = {self.id};
        COMMIT;
        """
        Bag.connectAndExecute(sql)

    def __str__(self):
        return f"Bag <{self.id}, {self.cost_id}, {self.client_id}, {self.cost}, {self.client}>"
