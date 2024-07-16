from dbconnection import result
from jsonschema import validate


class BAPTISM:

    __SCHEMA_BAPT = {
        "type": "object",
        "properties": {
            "baptism_no": {"type": "number"},
            "gochild":{"type":["string"]},
            "mother": {"type": ["string"]},
            "father": {"type": ["string"]},
            "file_url":{"type":["string"]}
        },
        "required": ["baptism_no","godchild", "mother", "father",'file_url' ]
    }

    def Add(self, data):  # add   new baptism record to databases
        try:
            validate(instance=data, schema=self.__SCHEMA_BAPT)
            query="""insert  into BAPTISM   ( BAPTISM_NO,godchild,MOTHER_NAMES,FATHER_NAMES,file_url,upload_time)
            VALUES(
            %(baptism_no)s,
            %(godchild)s,
            %(mother)s,
            %(father)s,
            %(file_url)s,
            now()
            )"""
            result.submit(query=query,params=data)
            print("success")
        except Exception as e:
            print(e)
            return e

    def update(self, data):  # edit baptism 
        try:
            validate(instance=data, schema=self.__SCHEMA_BAPT)
            query = """update  BAPTISM set  
            godchild =  %(godchild)s,
            MOTHER_NAMES = %(mother)s ,
            FATHER_NAMES = %(father)s 
            where BAPTISM_NO = %(baptism_no)s 
            """
            result.submit(query=query, params=data)
        except Exception as e:
            return e

    def get_all(self):
        return result.get("select * from BAPTISM  ",None)

    def get_by_no(self, BPT_NO):
        return result.get("select * from BAPTISM  WHERE BAPTISM_NO  = %s ",(BPT_NO,))

    def get(self,g_child,f_name,m_name ):
        if  m_name is not None:
            return result.get("select * from BAPTISM  WHERE godchild= %s and MOTHER_NAMES = %s ",(g_child,m_name))
        else:
            return result.get("select * from BAPTISM  WHERE godchild= %s and FATHER_NAMES = %s",(g_child,f_name))

    def delete(self,BPT_NO):
        return result.submit("delete from BAPTISM  WHERE BAPTISM_NO  = %s ",(BPT_NO,))


bptsm = BAPTISM()
# bptsm.edit_baptism({
#             "baptism_no":1,
#             "godchild":"sudan",
#             "mother": "vila no",
#             "father": "wiliam tano",
#             "file_url":"/huble/data"
#     })
# print(bptsm.baptism(g_child="sudan", f_name=None,m_name="vila no"))
