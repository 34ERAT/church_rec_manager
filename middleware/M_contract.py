from dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json

class DiSpensation:

    __SCHEMA_DISPENSATION = {
        "type": "object",
        "properties": {
            "M_CERT_NO":{type:"number"},
            "BY_CATHOLIC":{type:"string"},
            "DATE_":{type:"string",format:"date"},
            "LOCATION_ID":{type:"string"},
        }, 
        "required": ["CONTRANT_ID","M_CERT_NO","BY_CATHOLIC","DATE_","LOCATION_ID" ]
    }

    def new_person(self, data):
        try:
            validate(instance=data, schema=self.__SCHEMA_DISPENSATION)
            print("validation was a success")
        except Exception as e:
            return e

    def persons(self):
        print("i got all the DiSpensation record ")

    def person(self, pid):
        print("you have got record", pid)

    def delete(self):
        print("DiSpensation was deleted and all records related to the person")

prsn = DiSpensation();
