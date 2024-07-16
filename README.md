# THIS IS THE BACK END OF AND FRONT END OF CHURCH RECORD MANAGEMENT SYSTEM
The **church management system**  use *MYSQL* database as is core database management system  
and is developed on python on the **BACKEND**
# INSTALLATION
--
# usage
*** there are  ten middlewares for this module ***   and are pertty similar in functionality This functionality(methods ) includes   get_all, get, insert, delete and update
* **get_all**  :  retrives  all the records of the specified  record class
* **get** : retrives a single record from  takes the  record id as the parameters
* **insert** : inserts a single record  takes the record  dictionary  as a parameter
* **update** :  update an existing record 
* **delete** : deletes and existing record
###  person middleware 

* print(prsn.get("98f8c04e-1c27-11ef-a8d4-94b86de0e66a")) : *gets the record  using the id **"98f8c04e-1c27-11ef-a8d4-94b86de0e66a"** and prints the result*
* print(prsn.delete("98f8c04e-1c27-11ef-a8d4-94b86de0e66a")) :*deletes the record  using the id **"98f8c04e-1c27-11ef-a8d4-94b86de0e66a"** and prints the result*
* data = {
*     "FIRST_NAME": "alibama",
*     "LAST_NAME": "varma",
*     "DATE_OF_BIRTH": "2024-05-27",
*     "GENDER": "FEMALE",
*     "CLAN_ID": None,
* } :
* prsn.update(data,"5eb5c9b0-1c27-11ef-a8d4-94b86de0e66a")
* prsn.insert(data)
* print(prsn.get_all())
