/**procedure to insert into  marriage documents**/ 
select "marriage PROCEDURES";
drop procedure if exists insert_marriage  ;

delimiter $$

create procedure insert_marriage(
    date_ date, church_of varchar(50),banns_no int,
    delegate varchar(50),priest json,male_witness json,
    female_witness json,m_cert_no int
)
begin

	declare priest_id, male_witness_id ,female_witness_id varchar(255);

    declare exit  handler for sqlexception
    begin
        rollback;
        resignal;
    end;
    start transaction;
    /*insert priest*/
    if priest is not null then 
        set priest_id = uuid();
        call  json_insert_person(priest_id,godchild);
    end if;
    /*insert priest*/
    if male_witness is not null then 
        set male_witness_id = uuid();
      call  json_insert_person(uuid(),male_witness);
    end if;
    /*insert priest*/
    if female_witness is not null then 
        set female_witness_id = uuid();
      call  json_insert_person(uuid(),female_witness);
    end if;
    insert into MARRIAGE_(MARRIAGE_ID ,DATE_ , CHURCH_OF ,BANNS_NO ,DELEGATE ,PRIEST_ID ,MALE_WITNESS_ID ,FEMALE_WITNESS_ID ,M_CERT_NO )
    values(uuid(),date_ ,church_of,banns_no ,delegate,priest_id ,male_witness_id ,female_witness_id, m_cert_no );
    commit;
end $$
delimiter ;

