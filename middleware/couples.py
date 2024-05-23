from dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json


class Couples:

    _COUPLE = {
        "type": "object",
        "properties": {
            "M_CERT_NO": {"type": "string"},
            "PERSON_ID": {"type": "string"},
            "MOTHER_NAMES": {"type": "string"},
            "FATHER_NAMES": {"type": "string"},
            "DOMICILE": {"type": "string"}
        },
        "required": ["M_CERT_NO", "PERSON_ID", "MOTHER_NAMES", "FATHER_NAMES", "DOMICILE"]
    }

    def new_Couples(self, couple1, couple2):
        try:
            validate(instance=couple1, schema=self._COUPLE)
            validate(instance=couple2, schema=self._COUPLE)
            if couple1["M_CERT_NO"] == couple2["M_CERT_NO"]:
                print("couples are  to registered \n")
            else:
                print("couples will not be registered have different M_CERT_NO \n")

        except Exception as e:
            print(e, '\n')
            return e

    def couples(self):
        print("you have all the  couples")

    def couple(self, m_cert_no):
        print("couple")

    def delete(self):
        print("couple was deleted ")


couple = Couples()
couple1 = {
    "M_CERT_NO": "value sat",
    "PERSON_ID": "most carriage",
    "MOTHER_NAMES": "jari comb",
    "FATHER_NAMES": "alise",
    "DOMICILE": "value"
}
couple2 = {
    "M_CERT_NO": "value sat",
    "PERSON_ID": "most carriage",
    "MOTHER_NAMES": "jari comb",
    "FATHER_NAMES": "alise",
    "DOMICILE": "value"
}
couple.new_Couples(couple1=couple1, couple2=couple2)
