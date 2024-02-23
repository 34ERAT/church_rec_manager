/*procedure to  insert  insert _deaths*/
drop procedure if exists insert_death;

delimiter $$
create procedure insert_death(
    death_no int,pid varchar(255),so_or_do varchar(50),
    district_id varchar(255),baptism_id varchar(255),marriage_id varchar(255),
    last_rite enum('yes','no'), burial_place varchar(255),burial_date date,priest_id varchar(255)
)
begin
    insert into DEATHS (DEATH_ID,DEATH_NO,PID,SO_OR_DO,DISTRICT_ID,BAPTISM_ID,MARRIAGE_ID,last_rite,BURIAL_PLACE,BURIAL_DATE,priest_id ) 
    values( uuid(),death_no,pid,so_or_do,district_id,baptism_id,marriage_id,last_rite,burial_place,burial_date,priest_id )
end $$

delimiter ;

/*procedure to  edit person */
drop procedure if exists edit_death;

delimiter $$
create procedure edit_death (
    death_id varchar(255),death_no int,pid varchar(255),so_or_do varchar(50),
    district_id varchar(255),baptism_id varchar(255),marriage_id varchar(255),
    last_rite enum('yes','no'), b_place varchar(255),b_date date,priest_id varchar(255)
)
begin
    update DEATHS set  DEATH_NO = death_no , PID = pid , SO_OR_DO = so_or_do , DISTRICT_ID = district_id , 
    BAPTISM_ID = baptism_id , MARRIAGE_ID = marriage_id , last_rite = l_rite , BURIAL_PLACE = b_place , BURIAL_DATE = b_date , 
    priest_id = p_id  where DEATH_ID  =  death_id ;
end $$

delimiter ;

/*procedure to get   death_record*/
drop procedure if exists _death;

delimiter $$

create procedure _death (death_no int ,death_id varchar(255))
begin
    if death_no or death_id is null then

        select D.DEATH_NO , concat(P.FIRST_NAME " "P.LAST_NAME) as person_name , dis.LOC_NAME , 
        B.BAPTISM_NO,M.M_CERT_NO ,D.last_rite , L.LOC_NAME, D.BURIAL_DATE ,concat(v.FIRST_NAME " "v.LAST_NAME) as priest_name 
        from DEATHS  as D
        join (select PID ,FIRST_NAME , LAST_NAME  from  PERSONS  ) as P on D.PID = P.PID
        join BAPTISM as B on D.BAPTISM_ID = B.BAPTISM_ID
        join MARRIAGE_ as M  on D.MARRIAGE_ID = M.MARRIAGE_ID
        join LOCATION as L on D.BURIAL_PLACE = L.LOCATION_ID
        join (select PID ,FIRST_NAME , LAST_NAME  from  PERSONS ) as V on D.PID = V.PID
        where  D.DEATH_NO = death_no or DEATH_ID = death_id
    else
        select D.DEATH_NO , concat(P.FIRST_NAME " "P.LAST_NAME) as person_name  
        from DEATHS  as D
        join (select PID ,FIRST_NAME , LAST_NAME  from  PERSONS  ) as P on D.PID = P.PID
    end if;

end $$

delimiter ;
