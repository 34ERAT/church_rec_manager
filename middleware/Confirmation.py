from datetime import date
from dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json


class CONFIRMATION:

    __SCHEMA_confirm = {
        "type": "object",
        "properties": {
            "CONFIMATION_NO":{type:"number"},
            "DATE_":{type:"string"},
            "BAPTISM_ON:":{type:"number"},
            "NO_MEN_BAPT":{type:"string"},
            "G_mother":{type:"string"},
            "G_FATHER":{type:"string"},
            'PRIEST':{type:"string"},
            "BAPTUM_DIE":{type:"string"},
            "AT":{type:"string"},
            },
        "required": ["CONFIMATION_NO","DATE_","BAPTISM_ON:","NO_MEN_BAPT","G_mother","G_FATHER",'PRIEST',"BAPTUM_DIE", "AT"]
    }

    def new_Confirmation(self, data):
        try:
            validate(instance=data, schema=self.__SCHEMA_confirm)
            print("validation was a success")
        except Exception as e:
            return e

    def confrimations(self):
        print("i got all the baptism record ")

    def confirmation(self,baptism_no):
        print("you have got record",baptism_no)

confirmation = CONFIRMATION()
# data = {
#     "CONFIMATION_NO": 2342,
#     "DATE_": 'datetime',
#     "BAPTISM_ON:": 2342,
#     "NO_MEN_BAPT":"valuan" ,
#     "G_mother": 'vakaen' ,
#     "G_FATHER": "mostajkk",
#     'PRIEST':'akili' ,
#     "BAPTUM_DIE":'stamli' ,
#     "AT":"jlk" ,
# }
# print(confirmation.new_Confirmation(data))
# print(confirmation.confrimations())
