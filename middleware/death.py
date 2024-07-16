from jsonschema import validate
from dbconnection import result
import json

class Death:

    _DEATH = {
        "type": "object",
        "properties": {
            "Names": {"type": "string"},
            "file_url":{"type": "string"}
        },
        "required": ["Names","file_url"]
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
            result.submit(query=query,params=data)
        except Exception as e:
            return e

    def update(self,data):
        try:
            update_d = self._DEATH
            update_d['properties']['death_id'] ={"type": "string"}
            update_d['required'].append("death_id")
            validate(instance=data,schema=update_d)
            query="""update DEATH  set 
            Names= %(Names)s,
            file_url=%(file_url)s 
            where death_id=%(death_id)s
            """
            result.submit(query=query,params=data)
        except Exception as e:
            print(e)
            return e

    def get_all(self):
       return result.get("select * from DEATH d ;",None)

    def get(self, Names):
       return result.get("select * from DEATH  where  death_id= %s ;",(Names,))

    def delete(self,death_id):
       return result.submit("delete from DEATH  where  death_id= %s ;",(death_id,))

death = Death()

death.update({
    "death_id":'c9098f59-42b1-11ef-b796-94b86de0e66a',
    "Names": "valid jabali ",
    "file_url":"/boot/System.map-6.9.7-amd64/"
    })
print(death.get_all())
