from dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json
class Marriage:
    
    __MARRIAGE={
            "type":"object",
            "properties":{
                "date_":{
                         "type":"string",
                         "format":"date"
                         },
                "church_of":{"type":"string"},
                "banns_no":{"type":"number"},
                "delegate":SCHEMA_PRSN,
                "priest":SCHEMA_PRSN,
                "male_witness":SCHEMA_PRSN,
                "female_witness":SCHEMA_PRSN,
                "cert_no":{"type":"number"}
                },
            "required":["date_", "church_of", "banns_no","delegate", "priest", "male_witness", "female_witness", "cert_no"]
            }
    def new_marriage(self,data):
        try:
            validate(instance=data,schema=self.__MARRIAGE)
            data["delegate"]=json.dumps(data["delegate"])
            data["priest"]=json.dumps(data["priest"])
            data["male_witness"]=json.dumps(data["male_witness"])
            data["female_witness"]=json.dumps(data["female_witness"])
            #print(data);
            result.submit("""call insert_marriage(
                          %(date_)s,%(church_of)s,%(banns_no)s,%(delegate)s,
                          %(priest)s,%(male_witness)s,%(female_witness)s,%(cert_no)s)""",data)
            print("success")
        except Exception  as e :
            return e

mrage = Marriage();
# exmple of   how to  use the  new_marriage function 
# data={
#         "date_":"1954-02-23",
#         "church_of":"longont",
#         "banns_no":2342,
#         "delegate":{
#             "FIRST_NAME":"lakipata",
#             "LAST_NAME":"omosta",
#             "DATE_OF_BIRTH":"1934-01-23",
#             "GENDER":"female",
#             "CLAN_ID":"71348d02-024d-11ef-921e-94b86de0e66a"
#             },
#         "priest":{
#             "FIRST_NAME":"valimolit",
#             "LAST_NAME":"olamina",
#             "DATE_OF_BIRTH":"1964-01-23",
#             "GENDER":"male",
#             "CLAN_ID":"71348d02-024d-11ef-921e-94b86de0e66a"
#             },
#         "male_witness":{
#             "FIRST_NAME":"omarival",
#             "LAST_NAME":"kaptivi",
#             "DATE_OF_BIRTH":"2003-01-23",
#             "GENDER":"male",
#             "CLAN_ID":"71348d02-024d-11ef-921e-94b86de0e66a"
#             },
#         "female_witness":{
#             "FIRST_NAME":"kaplatm",
#             "LAST_NAME":"odowari",
#             "DATE_OF_BIRTH":"2003-01-23",
#             "GENDER":"female",
#             "CLAN_ID":"71348d02-024d-11ef-921e-94b86de0e66a"
#             },
#         "cert_no":232
#         }
# print(mrage.new_marriage(data)) 
