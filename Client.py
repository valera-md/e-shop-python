import psycopg2
from Model import Model

class Client(Model):
    
    def __init__(self, id, fullname, isvip):
        Model.__init__(self, id) # delegating constructor, делегировать конструктор
        self.fullname = fullname
        self.isvip = isvip

    def find(id):
        sql = f"""
        SELECT * FROM "clients" WHERE id = {id};
        """
        result = Client.connectAndExecute(sql, True)[0]
        c = Client(*result)
        return c

    def save(self):
        sql = f"""
        BEGIN;
        INSERT INTO "clients" VALUES({self.id}, {self.fullname}, '{self.isvip}');
        COMMIT;
        """
        Client.connectAndExecute(sql)

    def delete(self):
        sql = f"""
        BEGIN;
        DELETE FROM "clients" WHERE id = {self.id};
        COMMIT;
        """
        Client.connectAndExecute(sql)

    def update(self):
        sql = f"""
        BEGIN;
        UPDATE "clients" SET fullName = {self.fullname}, isvip = '{self.isvip}' WHERE id = {self.id};
        COMMIT;
        """
        Client.connectAndExecute(sql)

    def __str__(self):
        return f"Client <{self.id}, {self.fullname}, {self.isvip}>"
