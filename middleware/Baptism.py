import dbconnection as conn 

class BAPTISM:
    _CONN = conn.result
   def  __init__(self,baptism_no, godchild, mother, father, baptism_at, god_parent):
       self._CONN.submit('call insert_batism(%s, %s , %s, %s, %s , %s ) ')
