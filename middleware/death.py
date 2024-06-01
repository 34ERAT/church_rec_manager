from jsonschema import validate
from dbconnection import result
import json

class Death:

    _DEATH = {
        "type": "object",
        "properties": {
            "DEATH_NO": {"type": "number"},
            "PID": {"type": "string"},
            'SO_OR_DO': {"type": "string"},
            "last_rite": {"type": "string"},
            'BURIAL_PLACE': {"type":["string","null"]},
            "BURIAL_DATE": {
                "type": "string",
                "format": "date"
            },
            'priest_names': {"type": "string"}
        },
        "required": ['DEATH_NO',"PID","SO_OR_DO","last_rite","BURIAL_PLACE","BURIAL_DATE","priest_names"]
    }

    def new_death(self,data):
        try:
            validate(instance=data,schema=self._DEATH)
            query="""insert into DEATH (DEATH_NO,PID,SO_OR_DO,last_rite,BURIAL_PLACE,BURIAL_DATE,priest_names)
            values(%(DEATH_NO)s,%(PID)s,%(SO_OR_DO)s,%(last_rite)s,%(BURIAL_PLACE)s,%(BURIAL_DATE)s,%(priest_names)s)"""
            result.submit(query=query,params=data)
        except Exception as e:
            return e

    def edit_death(self,data):
        try:
            validate(instance=data,schema=self._DEATH)
            query="""update DEATH  set 
            PID =%(PID)s ,
            SO_OR_DO = %(SO_OR_DO)s,
            last_rite = %(last_rite)s,
            BURIAL_PLACE =%(BURIAL_PLACE)s ,
            BURIAL_DATE =%(BURIAL_DATE)s ,
            priest_names =%(priest_names)s where  DEATH_NO = %(DEATH_NO)s
            """
            result.submit(query=query,params=data)
            print("success")
        except Exception as e:
            print(e)
            return e

    def deaths(self):
       return result.get("select * from DEATH d ;",None)

    def death(self, DEATH_NO):
       return result.get("select * from DEATH  where  DEATH_NO = %s ;",(DEATH_NO,))

    def delete(self,DEATH_NO):
       return result.submit("delete from DEATH  where  DEATH_NO = %s ;",(DEATH_NO,))

death = Death()
# for x in range(4,10):
#     print(death.death(x))
#     data = {
#         "DEATH_NO": x,
#         "PID": "5ea88e42-1c27-11ef-a8d4-94b86de0e66a",
#         'SO_OR_DO': "value aout",
#         "last_rite": "NO",
#         'BURIAL_PLACE':None,
#         "BURIAL_DATE": '2023-04-24',
#         'priest_names': "valide"
#     }
#     death.edit_death(data)
#     death.new_death(data)

# print( death.deaths())

