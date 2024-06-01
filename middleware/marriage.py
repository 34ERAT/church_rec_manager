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
            query="""insert into MARRIAGE_  (M_CERT_NO,DATE_,CHURCH_OF,BANNS_NO,DELEGATE,PRIEST_NAMES,MALE_WITNESS,FEMALE_WITNESS)
            values( %(cert_no)s,%(date_)s, %(church_of)s, %(banns_no)s, %(delegate)s, %(priest)s, %(male_witness)s, %(female_witness)s);"""
            validate(instance=data,schema=self.__MARRIAGE)
            result.submit(query=query,params=data)
        except Exception  as e :
            print(e)
            return e

    def edit_marriage(self,data):
        try:
            query="""update MARRIAGE_  set  
            M_CERT_NO = %(cert_no)s,
            DATE_ = %(date_)s,
            CHURCH_OF = %(church_of)s,
            BANNS_NO = %(banns_no)s,
            DELEGATE = %(delegate)s,
            PRIEST_NAMES = %(priest)s,
            MALE_WITNESS = %(male_witness)s,
            FEMALE_WITNESS =%(female_witness)s where M_CERT_NO = %(cert_no)s"""
            validate(instance=data,schema=self.__MARRIAGE)
            result.submit(query=query,params=data)
        except Exception  as e :
            return e

    def Marriages(self):
        return  result.get("select * from MARRIAGE_  ", None)

    def Marriage(self,M_CERT_NO):
        return  result.get("select * from MARRIAGE_  where M_CERT_NO = %s ", (M_CERT_NO,))

    def delete (self,M_CERT_NO):
        return  result.submit("delete from MARRIAGE_  where M_CERT_NO = %s ", (M_CERT_NO,))

marriage = Marriage();
# for x in range(1,4):
#     data = {
#         "date_": "2024-04-02",
#         "church_of": "value mali",
#         "banns_no": 2343,
#         "delegate": "valandmalis",
#         "priest": "jari mlaina",
#         "male_witness": "mokaili maost",
#         "female_witness": "kanini afro",
#         "cert_no":x 
#     }
#     # marriage.edit_marriage(data)
#     # marriage.delete(x)
#     # print( marriage.Marriage(x))
#     # marriage.new_marriage(data)
#
# print(marriage.Marriages())
