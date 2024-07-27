from jsonschema import validate
from middleware.dbconnection import Connect


class Marriage:
    def __init__(self):
        self.result = Connect()
        self.__MARRIAGE = {
            "type": "object",
            "properties": {
                "marriage_id": {"type": "string"},
                "h_name": {"type": "string"},
                "w_name": {"type": "string"},
                "file_url": {"type": "string"},
            },
            "required": ["marriage_id", "h_name", "w_name", "file_url"]
        }

    def Add(self, data):
        try:
            query = """insert into MARRIAGE_  (marriage_id,h_name,w_name,upload_date,file_url)
            values( %(marriage_id)s,%(h_name)s, %(w_name)s,now(), %(file_url)s);"""
            validate(instance=data, schema=self.__MARRIAGE)
            self.result.submit(query=query, params=data)
        except Exception as e:
            print(e)
            return e

    def update(self, data):
        try:
            query = """update MARRIAGE_  set  
            marriage_id = %(marriage_id)s,
            h_name = %(h_name)s,
            w_name = %(w_name)s,
            file_url = %(file_url)s
            where marriage_id = %(marriage_id)s"""
            validate(instance=data, schema=self.__MARRIAGE)
            self.result.submit(query=query, params=data)
        except Exception as e:
            print(e)
            return e

    def get_all(self):
        return self.result.get("select marriage_id,h_name,w_name from MARRIAGE_  ", None)

    def get_by_id(self, marriage_id):
        return self.result.get("select marriage_id,h_name,w_name,file_url  from MARRIAGE_  where marriage_id= %s ", (marriage_id,))

    def get(self, h_name, w_name):
        return self.result.get("select * from MARRIAGE_  where h_name= %s and w_name =%s ", (h_name, w_name))

    def delete(self, marriage_id):
        return self.result.submit("delete from MARRIAGE_  where marriage_id= %s ", (marriage_id))


