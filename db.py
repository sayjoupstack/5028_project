import os
import psycopg2

class Databases():
    def __init__(self):
        self.db = psycopg2.connect(host=os.getenv("DB_HOST"), dbname=os.getenv("DB_DATABASE"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),port=5432)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()    