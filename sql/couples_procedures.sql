/*procedure to insert batism */
select "couple PROCEDURES";
drop procedure if exists insert_couple ;

delimiter $$

create procedure insert_couple(
  marriage_id varchar(255),
  bride json,
  mother  json,
  father json
)
begin

    declare exit handler for sqlexception
    begin
        rollback;
        resignal;
    end;
    start transaction;
    /*insert bride*/
    if bride is not null then 
      call  json_insert_person(uuid(),godchild);
    end if;

    /*insert mother*/
    if mother is not null then
      call  json_insert_person(uuid(),mother);
    end if;
    /*insert father*/
    if father is not null then 
       call json_insert_person(uuid(),father);
    end if;
    
    insert into BAPTISM (BAPTISM_ID ,BAPTISM_NO ,MOTHER_ID ,FATHER_ID ,BAPTISM_AT , g_PERSONS_ID )
    values(uuid() , baptism_no , godchild_id , mother_id , father_id , baptism_at , g_persons_id);
    commit;
end $$

delimiter ;
