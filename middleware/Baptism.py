from dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json


class BAPTISM:

    __SCHEMA_BAPT = {
        "type": "object",
        "properties": {
            "baptism_no": {"type": "number"},
            "godchild": {"type": ["string"]},
            "mother": {"type": ["string"]},
            "father": {"type": ["string"]},
            "baptism_at": {"type": ["string", "null"]},
            "god_father": {"type": ["string"]},
            "god_mother": {"type": ["string"]},
            "s_o_father": {"type": ["string", "null"]},
            "s_o_mother": {"type": ["string", "null"]}
        },
        "required": ["baptism_no", "godchild", "mother", "father", "baptism_at", "god_mother", "god_father", "s_o_mother", "s_o_father"]
    }

    def new_baptism(self, data):
        try:
            validate(instance=data, schema=self.__SCHEMA_BAPT)
            print("validation was a success")
        except Exception as e:
            return e

    def baptisms(self):
        print("i got all the baptism record ")

    def baptism(self, baptism_no):
        print("you have got record", baptism_no)

    def delete(self):
        print("baptism was deleted")


bptsm = BAPTISM()
# data = {
#     "baptism_no": 234,
#     "godchild": "jk23423432",
#     "mother": "salm",
#     "father": "japmih",
#     "baptism_at": "janai",
#     "god_father": "alimp",
#     "god_mother": "validate",
#     "s_o_father": "sfa",
#     "s_o_mother":"kanli"
# }
# print(bptsm.new_baptism(data));
# print(bptsm.baptisms())
