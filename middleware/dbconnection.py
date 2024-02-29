import  mysql.connector
import os
from dotenv import load_dotenv,dotenv_values 
load_dotenv()
class connect:
   ##__CONFIG = dotenv_values(".env")
   __CONNECTION =mysql.connector.connect(
           host=os.getenv("DB_HOST"),
           user=os.getenv('DB_USER'),
           password=os.getenv('DB_PASSWORD'),
           database=os.getenv('DB')
           )
   def submit_get(self,query):
      CURSOR=self.__CONNECTION.cursor()
      CURSOR.execute(query)
      return CURSOR.fetchall()

   def submit_add(self,query):
      CURSOR=self.__CONNECTION.cursor()
      CURSOR.execute(query)
      self.__CONNECTION.commit();
      return CURSOR.fetchall();

result = connect()

print(result.submit_get("show tables;"))

