from jsonschema import validate
from Church_rec_manager.middleware.dbconnection import connect
from Church_rec_manager.middleware.storefile import StoreFile
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

class BAPTISM:
    def __init__(self):
        self.connect =connect
        self.root_path = str(os.getenv('BAPTISM_ARCHIVE'))
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
            src_file= data["file_url"]
            final_dest =f"{self.root_path}/{data['baptism_no']}.jpg"
            data['file_url']=final_dest
            StoreFile(root_path=self.root_path,src=src_file,dest=final_dest)
            connect.submit(query=query, params=data)
        except Exception as e:
            print(e)
            raise e

    def update(self, data):  # edit baptism
        try:
            validate(instance=data, schema=self.__SCHEMA_BAPT)
            query = """update  BAPTISM set  
            godchild =  %(godchild)s,
            MOTHER_NAMES = %(mother)s ,
            FATHER_NAMES = %(father)s 
            where BAPTISM_NO = %(baptism_no)s 
            """
            src_file= data["file_url"]
            final_dest =f"{self.root_path}/{data['baptism_no']}.jpg"
            data['file_url']=final_dest
            StoreFile(root_path=self.root_path,src=src_file,dest=final_dest)
            
            self.connect.submit(query=query, params=data)
        except Exception as e:
            raise e

    def get_all(self,Limit=(0,20)):
        return self.connect.get(
            "select BAPTISM_NO ,godchild,MOTHER_NAMES,FATHER_NAMES from BAPTISM limit %s ,%s",
            Limit 
        )

    def get_by_no(self, BPT_NO):
        return self.connect.get(
            "select BAPTISM_NO ,godchild,MOTHER_NAMES,FATHER_NAMES , file_url from BAPTISM  WHERE BAPTISM_NO  = %s ", 
            (BPT_NO,)
        )

    def get(self, g_child, Parent):
        query = "select BAPTISM_NO ,godchild,MOTHER_NAMES,FATHER_NAMES from BAPTISM b  where godchild regexp %s and( b.MOTHER_NAMES regexp %s or b.FATHER_NAMES regexp %s );"
        if Parent is not None:
            return self.connect.get(query=query, params=(g_child, Parent, Parent))

    def delete(self, BPT_NO):
        return self.connect.submit("delete from BAPTISM  WHERE BAPTISM_NO  = %s ", (BPT_NO,))


