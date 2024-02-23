/*procedure to  insert clan */
drop procedure if exists insert_clan;

delimiter $$

create procedure insert_clan(  
   tribe_id  varchar(255),
   clan_name  varchar(50)
)
begin
    insert into CLAN (CID,TRIBE_ID,CLAN_NAME)
    values(uuid(),tribe_id,clan_name)
end $$

delimiter ;


/*procedure to  edit clan */
drop procedure if exists edit_clan;

delimiter $$

create procedure edit_clan(
   cid varchar(255)
   tribe_id  varchar(255),
   clan_name  varchar(50)
)
begin
    update CLAN set TRIBE_ID=tribe_id,CLAN_NAME=clan_name 
    where  CID = cid;
end $$

delimiter ;



/*procedure to  select clan */
drop procedure if exists select_clan;

delimiter $$

create procedure select_clan(
   cid varchar(255)
   tribe_id  varchar(255),
)
begin
    if cid and tribe_id is null then
        select C.CID, T.TRIBE_NAME, C.CLAN_NAME
        from CLAN as C  on TRIBE  as T  on C.TRIBE_ID = T.TRIBE_ID;

    elseif cid  is null then
        select C.CID, T.TRIBE_NAME, C.CLAN_NAME
        from CLAN as C  on TRIBE  as T  on C.TRIBE_ID = T.TRIBE_ID 
        where T.TRIBE_ID = tribe_id;

    elseif tribe_id is null then 
        select C.CID, T.TRIBE_NAME, C.CLAN_NAME
        from CLAN as C  on TRIBE  as T  on C.TRIBE_ID = T.TRIBE_ID 
        where C.CID = cid;

    else
        select C.CID, T.TRIBE_NAME, C.CLAN_NAME
        from CLAN as C  on TRIBE  as T  on C.TRIBE_ID = T.TRIBE_ID 
        where C.CID = cid and T.TRIBE_ID = tribe_id;
    end if;
end $$

delimiter ;


/*TRIBE PROCEDURES */

/*procedure to  insert tribe */
drop procedure if exists insert_tribe;

delimiter $$

create procedure insert_tribe(  
   tribe_name varchar(50)
)
begin
    insert into TRIBE (TRIBE_ID, TRIBE_NAME)
    values(uuid(),tribe_name)
end $$

delimiter ;

/*procedure to  edit tribe */
drop procedure if exists edit_tribe;

delimiter $$

create procedure edit_tribe(
   tribe_id  varchar(255),
   tribe_name  varchar(50)
)
begin
    update TRIBE set tribe_NAME=tribe_name 
    where  TRIBE_ID= tribe_id;
end $$

delimiter ;

