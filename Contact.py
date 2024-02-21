import psycopg2
from Model import Model
from Client import Client

class Contact(Model):
    
    def __init__(self, id, phoneNumber, emailAddress, client_id):
        Model.__init__(self, id) # delegating constructor, делегирование конструктора
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.client_id = client_id

    def find(id):
        sql = f"""
        SELECT * FROM "contacts" WHERE id = {id};
        """
        result = Contact.connectAndExecute(sql, True)[0]
        c = Contact(*result)
        cl = Client.find(result[3])
        c.client_data = cl
        return c

    def save(self):
        sql = f"""
        BEGIN;
        INSERT INTO "contacts" VALUES({self.id}, '{self.phoneNumber}', '{self.emailAddress}'), {client_id};
        COMMIT;
        """
        Contact.connectAndExecute(sql)

    def delete(self):
        sql = f"""
        BEGIN;
        DELETE FROM "contacts" WHERE id = {self.id};
        COMMIT;
        """
        Contact.connectAndExecute(sql)

    def update(self):
        sql = f"""
        BEGIN;
        UPDATE "contacts" SET phoneNumber = '{self.phoneNumber}', emailAddress = '{self.emailAddress}', client_id = {self.client_id} WHERE id = {self.id};
        COMMIT;
        """
        Contact.connectAndExecute(sql)

    def __str__(self):
        return f"Contact <{self.id}, {self.phoneNumber}, {self.emailAddress}, {self.client_id}, {self.client_data}>"
