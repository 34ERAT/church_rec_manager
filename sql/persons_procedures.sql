/*procedure to  insert  person */
select "persons PROCEDURES";
drop procedure if exists insert_person;

delimiter $$
create procedure insert_person(  
  first_name varchar(50),
  last_name varchar(50),
  date_of_birth date,
  gender enum('male','female'),
  clan_id varchar(255)
)
begin
    insert into PERSONS (PID,FIRST_NAME,LAST_NAME,DATE_OF_BIRTH,GENDER,CLAN_ID) 
    values( uuid(),first_name,last_name,date_of_birth,gender,clan_id);
end $$
delimiter ;

select "insert persons PROCEDURES";
drop procedure if exists insert_person;
delimiter $$
create procedure json_insert_person( in person_id varchar(255),in person json )
begin

    if person is not null then
        insert into PERSONS (PID,FIRST_NAME,LAST_NAME,DATE_OF_BIRTH,GENDER,CLAN_ID) 
        values( person_id,
            json_unquote(json_exctract(person,'$.FIRST_NAME')),
	        json_unquote(json_exctract(person,'$.LAST_NAME')),
	        json_unquote(json_exctract(person,'$.DATE_OF_BIRTH')),
	        json_unquote(json_exctract(person,'$.GENDER')),
	        json_unquote(json_exctract(person,'$.CLAN_ID'))
        );
    end if;
end $$
delimiter ;

select "editpersons PROCEDURES";
/*procedure to  edit person */
drop procedure if exists edit_person;
delimiter $$
create procedure edit_person(  
  pid varchar(255) ,
  first_name varchar(50),
  last_name varchar(50),
  date_of_birth date,
  gender enum('male','female'),
  clan_id varchar(255)
)
begin
    update PERSONS set FIRST_NAME=first_name,LAST_NAME=last_name,DATE_OF_BIRTH=date_of_birth,GENDER=gender,CLAN_ID=clan_id
    where  PID = pid;
end $$
delimiter ;
