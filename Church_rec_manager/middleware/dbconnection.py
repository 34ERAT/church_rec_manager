import mysql.connector
from mysql.connector import errorcode
import os
import sys
from dotenv import load_dotenv, dotenv_values

from Church_rec_manager.middleware.database_schema.Tables import TABLE_QUERIES
load_dotenv()


class Connect:
   # __CONFIG = dotenv_values(".env")
   def __init__(self):
       try:
           self.__CONNECTION = self.__NEW_CONNECTION()
       except mysql.connector.Error as error:
           if error.errno == errorcode.ER_BAD_DB_ERROR:
               print("Database does not exist. Attempting to create it...")
               cnx = mysql.connector.connect(
                   host=os.getenv("DB_HOST"),
                   user=os.getenv('DB_USER'),
                   password=os.getenv('DB_PASSWORD'),
               )
               cursor = cnx.cursor()
               cursor.execute(f"create database {os.getenv('DB')};")
               cnx.commit()
               cnx.database=os.getenv('DB')
               queries =TABLE_QUERIES()
               for query in queries.get_table_queries():
                    cursor.execute(query)
                    cnx.commit()
               cursor.close()
               self.__CONNECTION = self.__NEW_CONNECTION()

           if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                sys.exit(1)
           else:
                print("this is error result:::J ",error)
                sys.exit(1)

   def __NEW_CONNECTION(self):
       return mysql.connector.connect(
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
