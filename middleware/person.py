from logging import exception
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

    def new_person(self, data):  #adds anew person to database 
        try:
            validate(instance=data, schema=self.__SCHEMA_PRSN)
            query="""insert  into  PERSONS (PID,FIRST_NAME,LAST_NAME,DATE_OF_BIRTH,GENDER,CLAN_ID)
            VALUES(uuid(),%(FIRST_NAME)s,%(LAST_NAME)s,%(DATE_OF_BIRTH)s,%(GENDER)s,%(CLAN_ID)s)"""
            result.submit(query=query,params=data)
        except Exception as e:
            return e

    def edit_person(self, data, PID):  # adds anew person to database
        if (PID is not None):
            try:
                validate(instance=data, schema=self.__SCHEMA_PRSN) 
                data["PID" ] = PID
                query = """update  PERSONS set  
                FIRST_NAME = %(FIRST_NAME)s,
                LAST_NAME = %(LAST_NAME)s,
                DATE_OF_BIRTH = %(DATE_OF_BIRTH)s,
                GENDER = %(GENDER)s ,
                CLAN_ID = %(CLAN_ID)s 
                where PID = %(PID)s
                """
                result.submit(query=query, params=data)
            except Exception as e:
                return e
        else:
            print("PID is need ")

    def persons(self):
        return result.get("select *  from PERSONS p ;",None)

    def person(self, pid):
        return result.get("select *  from PERSONS where PID=%s ;",(pid,))

    def delete(self,pid):
        return result.submit("delete from PERSONS where PID=%s ;",(pid,))


prsn = Person()
# print(prsn.person("98f8c04e-1c27-11ef-a8d4-94b86de0e66a"))
# print(prsn.delete("98f8c04e-1c27-11ef-a8d4-94b86de0e66a"))
# data = {
#     "FIRST_NAME": "alibama",
#     "LAST_NAME": "varma",
#     "DATE_OF_BIRTH": "2024-05-27",
#     "GENDER": "FEMALE",
#     "CLAN_ID": None,
# }
# prsn.edit_person(data,"5eb5c9b0-1c27-11ef-a8d4-94b86de0e66a")
