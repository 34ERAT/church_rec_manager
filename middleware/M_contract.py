from dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json

class M_contract:

    __SCHEMA_DISPENSATION = {
        "type": "object",
        "properties": {
            "M_CERT_NO":{type:"number"},
            "BY_CATHOLIC":{type:"string"},
            "DATE_":{type:"string",format:"date"},
            "LOCATION_ID":{type:["string","null"]},
        }, 
        "required": ["M_CERT_NO","BY_CATHOLIC","DATE_","LOCATION_ID" ]
    }

    def new_contract(self, data):
        try:
            query= """insert into marriage_contract  (CONTRANT_ID,M_CERT_NO,BY_CATHOLIC,DATE_,LOCATION_ID)
            values(uuid(),%(M_CERT_NO)s,%(BY_CATHOLIC)s,%(DATE_)s,%(LOCATION_ID)s )"""
            validate(instance=data, schema=self.__SCHEMA_DISPENSATION)
            result.submit(query=query,params=data)
        except Exception as e:
            print(e)
            return e

    def edit_contract(self, data):
        try:
            query= """update  marriage_contract  set 
            BY_CATHOLIC = %(BY_CATHOLIC)s,
            DATE_ = %(DATE_)s,
            LOCATION_ID = %(LOCATION_ID)s  where M_CERT_NO = %(M_CERT_NO)s"""
            validate(instance=data, schema=self.__SCHEMA_DISPENSATION)
            result.submit(query=query,params=data)
        except Exception as e:
            print(e)
            return e

    def contracts(self):
        return result.get("select * from marriage_contract mc",None)

    def contract(self, Mcert):
        return result.get("select * from marriage_contract mc where M_CERT_NO = %s",(Mcert,))

    def delete(self,Mcert):
        return result.submit("delete  from marriage_contract mc where M_CERT_NO = %s",(Mcert,))
Contract = M_contract();
# for x in range(10):
#     data = {
#         "M_CERT_NO": x,
#         "BY_CATHOLIC":"NO",
#         "DATE_": "2023-04-03",
#         "LOCATION_ID": None,
#     }
#     # print(Contract.contract(x)) 
#     # Contract.new_contract(data)
#     # Contract.edit_contract(data)
#
# print(Contract.contracts())
