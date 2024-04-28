import  dbconnection as conn
from jsonschema import validate
DB_SUBMIT = conn.result
## new_clan 
# takes input in the form  of a dictinatiory  i.e
# TRIBE_ID="91e4914f-d73b-11ee-8358-94b86de0e66a",clan="MOSALI"
#
class  Clan:

    __SCHEMA={
            "type":"object",
 	        "properties":{
                "TRIBE_ID":{"type":"string"},
 	            "clan":{"type":"string"},
                },
            "required":["TRIBE_ID","clan"]
            }
    def new_clan(self,data):
        #validation schema for the data
        try:
            validate(instance=data,schema=self.__SCHEMA)
            return DB_SUBMIT.submit("call insert_clan(%(TRIBE_ID)s,%(clan)s)",(data))
        except Exception as e:
            return e

    def edit(self,data):
        try:
            validate(instance=data,schema=self.__SCHEMA)
            return DB_SUBMIT.submit("call insert_clan(%s,%s)",(data["TRIBE_ID"],data["clan"]))
        except Exception as e:
            return e

    def clan(self,clan_name):
        if clan_name is None:
            return None
        else:
            return DB_SUBMIT.get("""select t.TRIBE_NAME ,c.CLAN_NAME  from CLAN c join 
                                 TRIBE t  on c.TRIBE_ID  = t.TRIBE_ID  where CLAN_NAME  = %s""",(clan_name,))
    def clans(self):
        return DB_SUBMIT.get("""select t.TRIBE_NAME ,c.CLAN_NAME  from CLAN c join TRIBE t  on c.TRIBE_ID  = t.TRIBE_ID """,())

clan =  Clan()

print(clan.new_clan(dict(TRIBE_ID="91e4914f-d73b-11ee-8358-94b86de0e66a",claval="MOSALI")))
