from  dbconnection import result
from jsonschema import validate
from schemas.global_schemas import SCHEMA_PRSN
import json

class BAPTISM:

    __SCHEMA_BAPT={
            "type":"object",
            "properties":{
                "baptism_no":{"type":"number"},
                "godchild":SCHEMA_PRSN,
                "mother":SCHEMA_PRSN,
                "father":SCHEMA_PRSN,
                "baptism_at":{"type":["string","null"]},
                "god_parent":{
                    "type":["object","null"],
                    "properties":{
                        "god_father":SCHEMA_PRSN,
                        "god_mother":SCHEMA_PRSN,
                        "s_o_father":{"type":["string","null"]},
                        "s_o_mother":{"type":["string","null"]}
                        },
                    "required":["god_father","god_mother","s_o_father","s_o_mother"]
                    },
                },
            "required":["baptism_no","godchild","mother","father","baptism_at","god_parent"]
            }

    def new_baptism(self,data):
        try:
            validate(instance=data,schema=self.__SCHEMA_BAPT)
            data["godchild"]=json.dumps(data["godchild"])
            data["mother"]=json.dumps(data["mother"])
            data["father"]=json.dumps(data["father"])
            if data["god_parent"] is not None:
                data["god_parent"]=json.dumps(data["god_parent"])
                result.submit("call insert_batism(%(baptism_no)s,%(godchild)s,%(mother)s, %(father)s, %(baptism_at)s, %(god_parent)s)",data)
            else:
                result.submit("call insert_batism(%(baptism_no)s,%(godchild)s,%(mother)s, %(father)s, %(baptism_at)s, %(god_parent)s)",data)
                print("succeful")
        except Exception as e:
            return e

    def baptisms(self):
        slq="""
select b.BAPTISM_ID, concat(p3.FIRST_NAME ,' ', p3.LAST_NAME )  as god_child ,
	concat(p2.FIRST_NAME ,' ', p2.LAST_NAME )  as father,
 	concat(p.FIRST_NAME ,' ', p.LAST_NAME )  as mother,
 	g.G_FATHER_name,g.G_MOTHER_name
from BAPTISM b join
PERSONS p ON b.MOTHER_ID = p.PID
JOIN PERSONS p2 on b.FATHER_ID =p2.PID
join PERSONS p3 on b.G_CHILD = p3.PID
JOIN (
select gp.G_PERSONS_ID, gp.G_FATHER as G_FATHER_ID, 
CONCAT(p.FIRST_NAME ," ",p.LAST_NAME) as G_FATHER_name,
gp.G_MOTHER  as G_MOTHER_ID,
CONCAT(p2.FIRST_NAME ," ",p2.LAST_NAME) as G_MOTHER_name 
from G_PERSONS gp 
join PERSONS p  on gp.G_FATHER = p.PID  
join PERSONS p2  on gp.G_MOTHER  = p2.PID
) AS  g  ON  g.G_PERSONs_ID = b.g_PERSONS_ID ;

        """
        return   result.get(slq,())

bptsm = BAPTISM();
print(bptsm.baptisms())
 #ecord = {

 #       "baptism_no":2342,
 #       "godchild":{
 #           "FIRST_NAME":"JOSE",
 #           "LAST_NAME":"OMARI",
 #           "DATE_OF_BIRTH":"2004-01-23",
 #           "GENDER":"male",
 #           "CLAN_ID":"71348d02-024d-11ef-921e-94b86de0e66a"
 #       },
 #       "mother":{
 #           "FIRST_NAME":"BAKIJ",
 #           "LAST_NAME":"vOLLIA",
 #           "DATE_OF_BIRTH":"1994-01-23",
 #           "GENDER":"female",
 #           "CLAN_ID":"71348d02-024d-11ef-921e-94b86de0e66a"
 #       },
 #       "father":{
 #           "FIRST_NAME":"loki",
 #           "LAST_NAME":"ramadh",
 #           "DATE_OF_BIRTH":"1984-01-23",
 #           "GENDER":"female",
 #           "CLAN_ID":"71348d02-024d-11ef-921e-94b86de0e66a"
 #       },
 #       "baptism_at":None,
 #       "god_parent":None
 #       }
 #ptsm.new_baptism(record);
 

