from dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json
class Marriage:
    
    __MARRIAGE={
        "type": "object",
        "properties": {
            "marriage_id": {"type": "string"},
            "h_name": {"type": "string"},
            "w_name": {"type": "string"},
            "file_url": {"type": "string"},
        },
        "required": ["marriage_id", "h_name", "w_name", "file_url"]
    }

    def Add(self,data):
        try:
            query="""insert into MARRIAGE_  (marriage_id,h_name,w_name,upload_date,file_url)
            values( %(marriage_id)s,%(h_name)s, %(w_name)s,now(), %(file_url)s);"""
            validate(instance=data,schema=self.__MARRIAGE)
            result.submit(query=query,params=data)
        except Exception  as e :
            print(e)
            return e

    def update(self,data):
        try:
            query="""update MARRIAGE_  set  
            marriage_id = %(marriage_id)s,
            h_name = %(h_name)s,
            w_name = %(w_name)s,
            file_url = %(file_url)s
            where marriage_id = %(marriage_id)s"""
            validate(instance=data,schema=self.__MARRIAGE)
            result.submit(query=query,params=data)
        except Exception  as e :
            return e

    def get_all(self):
        return  result.get("select * from MARRIAGE_  ", None)

    def get(self,h_name,w_name):
        return  result.get("select * from MARRIAGE_  where h_name= %s and w_name =%s ", (h_name,w_name))

    def delete (self,marriage_id):
        return  result.submit("delete from MARRIAGE_  where marriage_id= %s ", (marriage_id))

marriage = Marriage();
marriage.update({
            "marriage_id": "you234",
            "h_name": "amo kip",
            "w_name": "viviam solo",
            "file_url": "/boot/System.map-6.9.7-amd64/",
            })
print(marriage.get_all())
