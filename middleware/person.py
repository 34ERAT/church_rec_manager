from dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json


class Person:

    __SCHEMA_PRSN = {
        "type": "object",
        "properties": {
            "FIRST_NAME": {type: "string"},
            "LAST_NAME": {type: "string"},
            "DATE_OF_BIRTH": {type: "string", format: "date"},
            "GENDER": {type: "string"},
            "CLAN_ID": {type: "string"},
        },
        "required": ["FIRST_NAME","LAST_NAME","DATE_OF_BIRTH","GENDER","CLAN_ID"]
    }

    def new_person(self, data):
        try:
            validate(instance=data, schema=self.__SCHEMA_PRSN)
            print("validation was a success")
        except Exception as e:
            return e

    def persons(self):
        print("i got all the baptism record ")

    def person(self, pid):
        print("you have got record", pid)

    def delete(self):
        print("person was deleted and all records related to the person")

prsn = Person();
