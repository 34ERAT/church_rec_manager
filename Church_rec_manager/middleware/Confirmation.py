from Church_rec_manager.middleware.dbconnection import connect
from jsonschema import validate


class CONFIRMATION:
    def __init__(self):
        self.result = connect
        self.__SCHEMA_confirm = {
            "type": "object",
            "properties": {
                "CONFIMATION_NO": {type: "number"},
                "DATE_": {type: "string", format: "date"},
                "BAPTISM_ON": {type: "number"},
                "NO_MEN_BAPT": {type: "number"},
                "G_mother": {type: "string"},
                "G_FATHER": {type: "string"},
                'PRIEST': {type: "string"},
                "BAPTUM_DIE": {type: "string"},
                "AT": {type: ["string", "null"]},
            },
            "required": ["CONFIMATION_NO", "DATE_", "BAPTISM_ON", "NO_MEN_BAPT", "G_mother", "G_FATHER", 'PRIEST', "BAPTUM_DIE", "AT"]
        }

    def new_Confirmation(self, data):
        try:
            validate(instance=data, schema=self.__SCHEMA_confirm)
            query="""insert into CONFIRMATION (CONFIMATION_NO,DATE_,BAPTISM_ON,NO_MEN_BAPT,G_mother,G_FATHER,PRIEST,BAPTUM_DIE,`AT`)
            values(%(CONFIMATION_NO)s,%(DATE_)s,%(BAPTISM_ON)s,%(NO_MEN_BAPT)s,%(G_mother)s,%(G_FATHER)s,%(PRIEST)s,%(BAPTUM_DIE)s, %(AT)s)"""
            self.result.submit(query=query,params=data)
        except Exception as e:
            return e

    def edit_Confirmation(self, data):
        try:
            validate(instance=data, schema=self.__SCHEMA_confirm)
            query="""update CONFIRMATION  set  
            DATE_= %(DATE_)s,
            BAPTISM_ON= %(BAPTISM_ON)s,
            NO_MEN_BAPT= %(NO_MEN_BAPT)s,
            G_mother= %(G_mother)s,
            G_FATHER=%(G_FATHER)s ,
            PRIEST=%(PRIEST)s ,
            BAPTUM_DIE= %(BAPTUM_DIE)s,
            `AT` = %(AT)s where  CONFIMATION_NO= %(CONFIMATION_NO)s"""
            self.result.submit(query=query,params=data)
        except Exception as e:
            return e

    def confrimations(self):
        return self.result.get("select * from CONFIRMATION  ",None)

    def confirmation(self,Conf_no):
        return self.result.get("select * from CONFIRMATION where CONFIMATION_NO = %s;", (Conf_no,))

    def delete(self,Conf_no):
        return self.result.submit("delete from CONFIRMATION   where CONFIMATION_NO = %s;", (Conf_no,))

# confirmation = CONFIRMATION()
# for x in range(4,10):
#     data = {
#         "CONFIMATION_NO": x,
#         "DATE_": '2003-04-20',
#         "BAPTISM_ON": 7,
#         "NO_MEN_BAPT": 4000,
#         "G_mother": 'vakaen',
#         "G_FATHER": "mostajkk",
#         'PRIEST': 'mostalai',
#         "BAPTUM_DIE": 'jarival',
#         "AT": "jlk",
#     }
#     print(confirmation.confirmation(x))
#     confirmation.delete(x)
#     confirmation.edit_Confirmation(data)
#     confirmation.new_Confirmation(data);
#
# print(confirmation.confrimations());
