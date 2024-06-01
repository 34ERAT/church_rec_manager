from dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json


class Couples:

    _COUPLE = {
        "type": "object",
        "properties": {
            "M_CERT_NO": {"type": "number"},
            "PERSON_ID": {"type": "string"},
            "MOTHER_NAMES": {"type": "string"},
            "FATHER_NAMES": {"type": "string"},
            "DOMICILE": {"type": "string"}
        },
        "required": ["M_CERT_NO", "PERSON_ID", "MOTHER_NAMES", "FATHER_NAMES", "DOMICILE"]
    }

    def new_Couples(self, couple1, couple2):
        try:
            query="""insert into COUPLES (C_MEMBER_ID,M_CERT_NO,PERSON_ID,MOTHER_NAMES,FATHER_NAMES,DOMICILE)
            values(uuid(),%(M_CERT_NO)s, %(PERSON_ID)s, %(MOTHER_NAMES)s, %(FATHER_NAMES)s, %(DOMICILE)s)"""
            validate(instance=couple1, schema=self._COUPLE)
            validate(instance=couple2, schema=self._COUPLE)
            if couple1["M_CERT_NO"] == couple2["M_CERT_NO"]:
                print("couples are  be to registered \n")
                result.submit(query=query,params=couple1);
                result.submit(query=query,params=couple2);
            else:
                print("couples will not be registered have different M_CERT_NO \n")
        except Exception as e:
            print(e, '\n')
            return e

    def edit_Couples(self, data):
        try:
            query="""update COUPLES set
			M_CERT_NO = %(M_CERT_NO)s, 
			MOTHER_NAMES = %(MOTHER_NAMES)s, 
			FATHER_NAMES = %(FATHER_NAMES)s , 
			DOMICILE = %(DOMICILE)s where PERSON_ID = %(PERSON_ID)s  """
            validate(instance=data, schema=self._COUPLE)
            result.submit(query=query,params=data);
        except Exception as e:
            print(e, '\n')
            return e

    def couples(self): 
        return result.get("select * from COUPLES  ",None)

    def couple(self, m_cert_no):
        return result.get("select * from COUPLES c WHERE c.M_CERT_NO =%s",(m_cert_no,))

    def delete(self,m_cert_no):
        return result.submit("delete from COUPLES c WHERE c.M_CERT_NO = %s",(m_cert_no,))


couple = Couples()
# for x in range(4,10):
#     couple1 = {
#         "M_CERT_NO": x,
# 	    "PERSON_ID": "5eb5c9b0-1c27-11ef-a8d4-94b86de0e66a",
#         "MOTHER_NAMES": "avila data most",
# 	    "FATHER_NAMES": "alise",
# 	    "DOMICILE":" come homw to you "
#     }
#     couple2 = {
#         "M_CERT_NO": x,
# 	    "PERSON_ID": "99c0c752-1c27-11ef-a8d4-94b86de0e66a",
# 	    "MOTHER_NAMES": "jari comb",
# 	    "FATHER_NAMES": "alise",
# 	    "DOMICILE": "value"
#     }
#     couple.edit_Couples(couple1)
#     # print(couple.couple(x)) 
#     # couple.new_Couples(couple1=couple1, couple2=couple2)
#
# print(couple.couples());
