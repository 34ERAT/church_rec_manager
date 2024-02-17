# THIS IS THE BACK END OF AND FRONT END OF CHURCH RECORD MANAGEMENT SYSTEM
The **church management system**  used *MYSQL* database as is core database management system  
and is developed on python on the **BACKEND**

## DATABASE PROCEDURES 

### -   PERSONS PROCEDURES

**insert_person** this inserts  a person int he persons table and return the  person id when   the  person is inserted successfull
it takes person details as the parameters
**i.e:** *insert_person([first_name],[second_name],[data_of_brith],[GENDER],[clan_name],[tribe_name]);*

### -   LOCATION PROCEDURES
- location
**get_location_id** this return the location id if the location exist it takes two inputs *location name  and district name*
**i.e:** *get_location_id([location name],[district name])*

**locations** this return all location of a given district takes district name as the parameter
**i.e** *location([district name])*

### -   PARENTS PROCEDURES
**insert_parent** this insert records into the parants table and return  parants id asign to them  it takes two parameters *fathers_id* and  *mothers id*
the father and mother id are  from the  the person tables 
**i.e:** *insert_parent([father id ] , [mother id]);*

### -  PRIESTS PROCEDURES
**insert_priest** this insert  priest_id into the database and it  returns the priest_id it also takes the following details  [first name],[second name],[ date of birth], [gender]
 **i.e:** *insert_priest([first name],[second name],[ date of birth], [gender],[clan_namej],[tribe_name]);*

### -  MARRIAGE PROCEDURES

**insert_marriage** this inserts marriage record into the database and returns a generated marriage id
**i.e** *insert_marriage([date],[church of],[DISP_ID],[DELEGATE(PERSONS_ID)],[PRIEST_ID],[M_CERT_NO]);*

**insert_dispensation** this insert the DISPENSATION record to the database and returns a DISP_ID 
**i.e:** *insert_despensation([D_FROM],[GIVEN_BY],[EMPEPIMENTS_OF],[Date_],[LOCATION_ID]);*

**get_marriage** this  procedure return on marriage record if the marriage number is specified and  
when not specified it return all the marriage record . The method only takes one parameter
**i.e:** *get_marriage([marriage_NO]) this return one record only* **or** *get_marriage([null]) this return all record form the database*

### -  TRIBE AND CLAN PROCEDURES
**insert_tribe** this is used to insert  tribe into the database  and return the generated tribe id  
**i.e:** *insert_tribe([tribe_name])*

**insert_clan** this is used to insert the clan details to the database and return the generate clan_id , this procedure takes two parameters
if the tribe does_not exist in the database the  procedure will create  one and  with the specified name
**i.e:** *insert_clan([clan name],[tribe id]);*

**get_clan_id** this returns the clan id  if the clan exists it takes  two inputs *clan name and tribe name*
**i.e:** *get_clan_id([clan name],[tribe name])*

## - BAPTISM PROCEDURES
**get_baptism** this  procedure return on baptism record if the baptism number is specified and  
when not specified it return all the baptism record . The method only takes one parameter
**i.e:** *get_baptism([BAPTISM_NO]) this return one record only* **or** *get_baptism([null]) this return all record form the database*

## - DEATH PROCEDURES
**get_death** this procedure returns one death record if the  death no is specified  else it return all of the records.
The method only takes one parameter
**i.e:** *get_death([death_NO]) this return one record only* **or** *get_death([null]) this return all record form the database*

## - CONFIMATION PROCEDURES

**get_confirmation** this procedure returns one confirmation record if the  confirmation no is specified  else it return all of the records.
The method only takes one parameter
**i.e:** *get_confirmation([confirmation_NO]) this return one record only* **or** *get_confirmation([null]) this return all record form the 
database*



