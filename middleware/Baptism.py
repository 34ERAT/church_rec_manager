from jsonschema import validate
from middleware.dbconnection import Connect

class BAPTISM:
    def __init__(self):
        self.result = Connect()
        self.__SCHEMA_BAPT = {
            "type": "object",
            "properties": {
                "baptism_no": {"type": "number"},
                "godchild": {"type": ["string"]},
                "mother": {"type": ["string"]},
                "father": {"type": ["string"]},
                "file_url": {"type": ["string"]}
            },
            "required": ["baptism_no", "godchild", "mother", "father", 'file_url']
        }

    def Add(self, data):  # add   new baptism record to databases
        try:
            validate(instance=data, schema=self.__SCHEMA_BAPT)
            query = """insert  into BAPTISM   ( BAPTISM_NO,godchild,MOTHER_NAMES,FATHER_NAMES,file_url,upload_time)
            VALUES(
            %(baptism_no)s,
            %(godchild)s,
            %(mother)s,
            %(father)s,
            %(file_url)s,
            now()
            )"""
            self.result.submit(query=query, params=data)
        except Exception as e:
            return e

    def update(self, data):  # edit baptism
        try:
            validate(instance=data, schema=self.__SCHEMA_BAPT)
            query = """update  BAPTISM set  
            BAPTISM_NO = %(baptism_no)s 
            godchild =  %(godchild)s,
            MOTHER_NAMES = %(mother)s ,
            FATHER_NAMES = %(father)s 
            where BAPTISM_NO = %(baptism_no)s 
            """
            self.result.submit(query=query, params=data)
        except Exception as e:
            return e

    def get_all(self):
        return self.result.get("select * from BAPTISM  ", None)

    def get_by_no(self, BPT_NO):
        return self.result.get("select * from BAPTISM  WHERE BAPTISM_NO  = %s ", (BPT_NO,))

    def get(self, g_child, Parent):
        query = "select * from BAPTISM b  where godchild = %s and( b.MOTHER_NAMES = %s or b.FATHER_NAMES = %s );"
        if Parent is not None:
            # return result.get(query=query,params=None)
            return self.result.get(query=query, params=(g_child, Parent, Parent))
        #     return result.get("select * from BAPTISM  WHERE godchild= %s and MOTHER_NAMES= %s",(g_child,Parent))

    def delete(self, BPT_NO):
        return self.result.submit("delete from BAPTISM  WHERE BAPTISM_NO  = %s ", (BPT_NO,))


