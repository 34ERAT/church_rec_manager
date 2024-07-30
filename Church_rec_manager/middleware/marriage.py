from jsonschema import validate
from Church_rec_manager.middleware.dbconnection import connect
from Church_rec_manager.middleware.storefile import StoreFile
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

class Marriage:
    def __init__(self):
        self.connect = connect
        self.root_path = str(os.getenv('MARRIAGE_ARCHIVE'))
        self.__MARRIAGE = {
            "type": "object",
            "properties": {
                "marriage_id": {"type": "string"},
                "h_name": {"type": "string"},
                "w_name": {"type": "string"},
                "file_url": {"type": "string"},
            },
            "required": ["marriage_id", "h_name", "w_name", "file_url"]
        }

    def Add(self, data):
        try:
            query = """insert into MARRIAGE_  (marriage_id,h_name,w_name,upload_date,file_url)
            values( %(marriage_id)s,%(h_name)s, %(w_name)s,now(), %(file_url)s);"""
            validate(instance=data, schema=self.__MARRIAGE)

            src_file= data["file_url"]
            final_dest =f"{self.root_path}/{data['marriage_id']}.jpg"
            data['file_url']=final_dest
            StoreFile(root_path=self.root_path,src=src_file,dest=final_dest)
            self.connect.submit(query=query, params=data)

        except Exception as e:
            print(e)
            raise e

    def update(self, data):
        try:
            query = """update MARRIAGE_  set  
            marriage_id = %(marriage_id)s,
            h_name = %(h_name)s,
            w_name = %(w_name)s,
            file_url = %(file_url)s
            where marriage_id = %(marriage_id)s"""
            validate(instance=data, schema=self.__MARRIAGE)

            src_file= data["file_url"]
            final_dest =f"{self.root_path}/{data['marriage_id']}.jpg"
            data['file_url']=final_dest
            StoreFile(root_path=self.root_path,src=src_file,dest=final_dest)

            self.connect.submit(query=query, params=data)
        except Exception as e:
            print(e)
            raise e

    def get_all(self,Limit=(0,20)):
        return self.connect.get("select marriage_id,h_name,w_name from MARRIAGE_ limit %s,%s ", Limit)

    def get_by_id(self, marriage_id):
        return self.connect.get("select marriage_id,h_name,w_name,file_url  from MARRIAGE_  where marriage_id= %s ", (marriage_id,))

    def get(self, h_name, w_name):
        return self.connect.get("select marriage_id,h_name,w_name  from MARRIAGE_  where h_name regexp  %s and w_name  regexp %s ", (h_name, w_name))

    def delete(self, marriage_id):
        return self.connect.submit("delete from MARRIAGE_  where marriage_id= %s ", (marriage_id,))


