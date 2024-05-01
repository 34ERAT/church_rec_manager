
SCHEMA_PRSN={
            "type":["object","null"],
            "properties":{
                "FIRST_NAME":{"type":"string"},
                "LAST_NAME":{"type":"string"},
                "DATE_OF_BIRTH":{
                    "type":"string",
                    "format":"date"
                    },
                "GENDER":{"type":"string"},
                "CLAN_ID":{"type":"string"},
                },
            "required":["FIRST_NAME","LAST_NAME","DATE_OF_BIRTH","GENDER","CLAN_ID"]
            }
