from dbconnection import result
from jsonschema import validate


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

    def new_baptism(self, data):  # add   new baptism record to databases
        try:
            validate(instance=data, schema=self.__SCHEMA_BAPT)
            query="""insert  into BAPTISM   ( BAPTISM_NO,godchild,MOTHER_NAMES,FATHER_NAMES,BAPTISM_AT,G_MOTHER,G_FATHER,s_o_g_mother,s_o_g_father)
            VALUES(
            %(baptism_no)s, %(godchild)s, %(mother)s,
            %(father)s, %(baptism_at)s,%(god_mother)s,
            %(god_father)s, %(s_o_mother)s, %(s_o_father)s
            )"""
            result.submit(query=query,params=data)
            print("success")
        except Exception as e:
            print(e)
            return e

    def edit_baptism(self, data):  # edit baptism 
        try:
            validate(instance=data, schema=self.__SCHEMA_BAPT)
            query = """update  BAPTISM set  
            godchild =  %(godchild)s,
            MOTHER_NAMES = %(mother)s ,
            FATHER_NAMES = %(father)s,
            BAPTISM_AT =  %(baptism_at)s,
            G_MOTHER = %(god_mother)s,
            G_FATHER = %(god_father)s,
            s_o_g_mother = %(s_o_mother)s,
            s_o_g_father = %(s_o_father)s where BAPTISM_NO = %(baptism_no)s """
            result.submit(query=query, params=data)
        except Exception as e:
            return e

    def baptisms(self):
        return result.get("select * from BAPTISM  ",None)

    def baptism(self, BPT_NO):
        return result.get("select * from BAPTISM  WHERE BAPTISM_NO  = %s ",(BPT_NO,))

    def delete(self,BPT_NO):
        return result.submit("delete from BAPTISM  WHERE BAPTISM_NO  = %s ",(BPT_NO,))


bptsm = BAPTISM()
# for x in range(4,10):
#     data = {
#         "baptism_no": x,
#         "godchild": "5edb6036-1c27-11ef-a8d4-94b86de0e66a",
#         "mother": "va234234lued",
#         "father": "moskkjljljlkt",
#         "baptism_at": None,
#         "god_father": "alimp",
#         "god_mother": "validate",
#         "s_o_father": "sfa",
#         "s_o_mother": "kanli"
#     }
#     bptsm.edit_baptism(data)
#
#
# print(bptsm.baptisms())
#
