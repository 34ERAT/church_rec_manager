import  mysql.connector
from dotenv import dotenv_values
class  connect:
    __CONFIG = dotenv_values(".env")
    __CONNECTION =mysql.connector.connect(
            host=__CONFIG['DB_HOST'],
            user=__CONFIG['DB_USER'],
            password=__CONFIG['DB_PASSWORD'],
            database=__CONFIG['DB']
            )
    def submit(self,query):
       CURSOR=self.__CONNECTION.cursor()
       CURSOR.execute(query)
       return CURSOR

result = connect()


print(result.submit("show tables;").fetchall())

