from jsonschema import validate
from Church_rec_manager.middleware.dbconnection import connect
import os
from dotenv import load_dotenv, dotenv_values

from Church_rec_manager.middleware.storefile import StoreFile
load_dotenv()

class Death:
    def __init__(self):
        self.connect = connect
        self.root_path = str(os.getenv('DEATH_ARCHIVE'))
        self._DEATH = {
            "type": "object",
            "properties": {
                "Names": {"type": "string"},
                "file_url": {"type": "string"}
            },
            "required": ["Names", "file_url"]
        }

    def Add(self,data):
        try:
            validate(instance=data,schema=self._DEATH)
            query="""insert into DEATH (death_id,Names,upload_date,file_url)
            values(
            uuid(),
            %(Names)s,
            now(),
            %(file_url)s
            )"""
            src_file= data["file_url"]
            final_dest =f"{self.root_path}/{data['Names']}.jpg"
            data['file_url']=final_dest
            StoreFile(root_path=self.root_path,src=src_file,dest=final_dest)
            self.connect.submit(query=query,params=data)
        except Exception as e:
            print(e)
            raise e

    def update(self,data):
        try:
            update_d = self._DEATH
            update_d['properties']['death_id'] ={"type": "string"}
            update_d['required'].append("death_id")
            query="""update DEATH  set 
            Names= %(Names)s,
            file_url=%(file_url)s 
            where death_id=%(death_id)s
            """
            src_file= data["file_url"]
            final_dest =f"{self.root_path}/{data['Names']}.jpg"
            data['file_url']=final_dest
            StoreFile(root_path=self.root_path,src=src_file,dest=final_dest)

            self.connect.submit(query=query,params=data)
        except Exception as e:
            print(e)
            raise e

    def get_all(self, Limit=(0,20)):
       return self.connect.get("select death_id, Names from DEATH d limit %s,%s;",Limit)

    def get_by_id(self, id):
       return self.connect.get("select death_id,Names,file_url from DEATH  where  death_id= %s ;",(id,))

    def get(self, Name):
       return self.connect.get("select death_id,Names,file_url from DEATH  where  Names regexp %s ;",(Name,))

    def delete(self,death_id):
       return self.connect.submit("delete from DEATH  where  death_id= %s ;",(death_id,))

