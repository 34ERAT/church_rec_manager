from dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json

class DiSpensation:

    __SCHEMA_DISPENSATION = {
        "type": "object",
        "properties": {
            "M_CERT_NO": {type: "number"}, 
            "D_FROM": {type: "string"}, 
            "GIVEN_BY": {type: "string"}, 
            "EMPEPIMENTS_OF": {type: "string"}, 
            "DATE_": {type: "string", format: "date"}, 
            "LOCATION_ID": {type:[ "string","null"]},
        }, 
        "required": [ "M_CERT_NO", "D_FROM", "GIVEN_BY", "EMPEPIMENTS_OF",  "DATE_", "LOCATION_ID"]
    }

    def new_DISP(self, data):
        try:
            query = """insert into DISPENSATION (DISP_ID,M_CERT_NO,D_FROM,GIVEN_BY,EMPEPIMENTS_OF,DATE_,LOCATION_ID)
            values(uuid(), %(M_CERT_NO)s, %(D_FROM)s, %(GIVEN_BY)s, %(EMPEPIMENTS_OF)s,  %(DATE_)s, %(LOCATION_ID)s)"""
            validate(instance=data, schema=self.__SCHEMA_DISPENSATION)
            result.submit(query=query,params=data)
        except Exception as e:
            print(e)
            return e

    def edit_DISP(self, data):
        try:
            query = """update DISPENSATION set 
            M_CERT_NO =%(M_CERT_NO)s ,
            D_FROM = %(D_FROM)s,
            GIVEN_BY =  %(GIVEN_BY)s,
            EMPEPIMENTS_OF = %(EMPEPIMENTS_OF)s,
            DATE_ = %(DATE_)s,
            LOCATION_ID = %(LOCATION_ID)s where M_CERT_NO =%(M_CERT_NO)s  """
            validate(instance=data, schema=self.__SCHEMA_DISPENSATION)
            result.submit(query=query,params=data)
        except Exception as e:
            print(e)
            return e

    def DISPs(self):
        return result.get("select * from DISPENSATION ;",None)

    def DISP(self, M_CERT_NO):
        return result.get("select * from DISPENSATION  where M_CERT_NO = %s",(M_CERT_NO,))

    def delete(self,M_CERT_NO):
        return result.submit("select * from DISPENSATION  where M_CERT_NO = %s",(M_CERT_NO,))

Disp = DiSpensation();
# for x in range(10):
#     data = {
#         "M_CERT_NO": x, 
#         "D_FROM": "janrava data base", 
#         "GIVEN_BY":"amos " , 
#         "EMPEPIMENTS_OF":"omata limses" , 
#         "DATE_": "2024-02-23", 
#         "LOCATION_ID": None
#     }
#     print(Disp.DISP(x)) 
#     # Disp.edit_DISP(data);
#     # Disp.new_DISP(data)
#
# print(Disp.DISPs())
