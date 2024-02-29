/*procedure to insert batism */
drop procedure if exists insert_batism ;

delimiter $$

create procedure insert_batism(
    baptism_no int, godchild json ,mother json,
    father json,baptism varchar(255), god_parent json)
begin
    declare god_father json;
    declare god_mather json;
    declare godchild_id , mother_id ,father_id  varchar(255);
    declare g_persons_id, god_father_id ,god_mother_id varchar(255);

    declare exit handler for sqlexception
    begin
        rollback;
        resignal;
    end;
    start transaction;
    /*insert godchild*/
    if godchild is not null then 
        set godchild_id = uuid();
       call json_insert_person(godchild_id,godchild);
    end if;

    /*insert mother*/
    if mother is not null then
        set mother_id = uuid();
       call json_insert_person(mother_id ,mother);
    end if;
    /*insert father*/
    if father is not null then 
        set father_id = uuid();
       call json_insert_person(father_id ,father);
    end if;
    /*insert god_parent*/
    if god_parent is not null then 

    /*insert god_father*/
        set god_father = json_exctract(god_parent,'$.god_father');
        set god_father_id= uuid();
       call json_insert_person(god_father_id ,god_father);

    /*insert god_mohter*/
        set god_mother_id= uuid();
        set god_father =json_exctract(god_parent,'$.god_mother');
       call json_insert_person(god_mother_id ,god_mother);
        insert into G_PERSONS(G_PERSONS_ID,G_FATHER,S_O_father,G_MOTHER,S_O_mother)
        values(g_persons_id,god_father_id,
	        json_unqute(json_exctract(god_parent,'$.s_o_father')),
            god_mother_id,
	        json_unqute(json_exctract(god_parent,'$.s_o_mother'))
        );
    end if;
    
    insert into BAPTISM (BAPTISM_ID ,BAPTISM_NO ,MOTHER_ID ,FATHER_ID ,BAPTISM_AT , g_PERSONS_ID )
    values(uuid() , baptism_no , godchild_id , mother_id , father_id , baptism_at , g_persons_id);
    commit;
end $$

delimiter ;
