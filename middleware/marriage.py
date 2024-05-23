from dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json
class Marriage:
    
    __MARRIAGE={
        "type": "object",
        "properties": {
            "date_": {
                    "type": "string",
                    "format": "date"
            },
            "church_of": {"type": "string"},
            "banns_no": {"type": "number"},
            "delegate": {"type": "string"},
            "priest": {"type": "string"},
            "male_witness": {"type": "string"},
            "female_witness": {"type": "string"},
            "cert_no": {"type": "number"}
        },
        "required": ["date_", "church_of", "banns_no", "delegate", "priest", "male_witness", "female_witness", "cert_no"]
    }
    def new_marriage(self,data):
        try:
            validate(instance=data,schema=self.__MARRIAGE)
            print("success")
        except Exception  as e :
            return e

    def Marriages(self):
        print("most value you got all marriages")

    def Marriage(self,data):
        print("got marriage")

mrage = Marriage();
data = {
    "date_": "24-03-2024",
    "church_of": "value mali",
    "banns_no":2343,
    "delegate": "valune malis",
    "priest": "jari most",
    "male_witness": "value maost",
    "female_witness": "kanini jana",
    "cert_no":23423
}
mrage.new_marriage(data)
