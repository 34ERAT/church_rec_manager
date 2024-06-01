import  dbconnection as conn
from jsonschema import validate
DB_SUBMIT = conn.result
class  Clan:

    __SCHEMA = {
        "type": "object",
        "properties": {
                "TRIBE_ID": {"type": "string"},
            "clan": {"type": "string"},
        },
        "required": ["TRIBE_ID", "clan"]
    }

    def new_clan(self, data):
        # validation schema for the data
        try:
            validate(instance=data, schema=self.__SCHEMA)
            query="insert into clan (CID,TRIBE_ID,CLAN_NAME) values(uuid(),%(TRIBE_ID)s,%(clan)s) "
            return DB_SUBMIT.submit(query=query, params=data)
        except Exception as e:
            return e

    def edit(self, data,cid):
        try:
            validate(instance=data, schema=self.__SCHEMA)
            data["cid"] = cid
            query="update clan set TRIBE_ID = %(TRIBE_ID)s,CLAN_NAME = %(clan)s where CID = %(cid)s"
            return DB_SUBMIT.submit(query, data)
        except Exception as e:
            return e

    def clan(self, clan_name):
        if clan_name is None:
            return None
        else:
            return DB_SUBMIT.get("""select t.TRIBE_NAME ,c.CLAN_NAME  from CLAN c join 
                                 TRIBE t  on c.TRIBE_ID  = t.TRIBE_ID  where CLAN_NAME  = %s""", (clan_name,))

    def clans(self):
        return DB_SUBMIT.get("""select t.TRIBE_NAME ,c.CLAN_NAME  from CLAN c join TRIBE t  on c.TRIBE_ID  = t.TRIBE_ID """, ())

clan =  Clan()
print(clan.clans())

