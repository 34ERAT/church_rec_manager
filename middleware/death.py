from jsonschema import validate
from middleware.dbconnection import Connect
# from dbconnection import result

class Death:
    def __init__(self):
        self.result = Connect()
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
            self.result.submit(query=query,params=data)
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
            self.result.submit(query=query,params=data)
        except Exception as e:
            print(e)
            return e

    def get_all(self):
       return self.result.get("select death_id, Names from DEATH d ;",None)

    def get_by_id(self, id):
       return self.result.get("select death_id,Names,file_url from DEATH  where  death_id= %s ;",(id,))

    def delete(self,death_id):
       return self.result.submit("delete from DEATH  where  death_id= %s ;",(death_id,))

