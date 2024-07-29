import mysql.connector
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()


class Connect:
   # __CONFIG = dotenv_values(".env")
   def __init__(self):
       self.__CONNECTION = mysql.connector.connect(
           host=os.getenv("DB_HOST"),
           user=os.getenv('DB_USER'),
           password=os.getenv('DB_PASSWORD'),
           database=os.getenv('DB')
       )

   def get(self, query, params):
       CURSOR = self.__CONNECTION.cursor(prepared=True)
       CURSOR.execute(query, params)
       data = CURSOR.fetchall()
       CURSOR.close()
       return data

   def submit(self, query, params):
       CURSOR = self.__CONNECTION.cursor(prepared=True)
       CURSOR.execute(query, params)
       self.__CONNECTION.commit()
       result = CURSOR.fetchall()
       CURSOR.close()
       return result

connect = Connect()
