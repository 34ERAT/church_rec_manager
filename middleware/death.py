from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json

class Death:

    _DEATH = {
        "type": "object",
        "properties": {
            "DEATH_NO": {"type": "number"},
            "PID": {"type": "string"},
            'SO_OR_DO': {"type": "string"},
            "last_rite": {"type": "string"},
            'BURIAL_PLACE': {"type": "string"},
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
            print("success")
        except Exception as e:
            print(e)
            return e

    def deaths(self):
        print("you have all the  deaths")

    def death(self, DEATH_NO):
        print("death")

    def delete(self):
        print("death was deleted ")

date = Death()
data = {
    "DEATH_NO": 234,
    "PID": "somoi",
    'SO_OR_DO': "mali",
    "last_rite": "javali",
    'BURIAL_PLACE': "home mali",
    "BURIAL_DATE": '25-09-2023',
    'priest_names':"valide" 
}
date.new_death(data)
