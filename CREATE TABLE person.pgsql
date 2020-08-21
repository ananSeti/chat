DROP TABLE iF EXISTS person;
DROP TATBLE IF EXISTS history;

CREATE TABLE person(
    id SERIAL PRIMARY KEY ,
    first_name TEXT not NULL,
    last_name TEXT, 
    birthday date,
    sex  INTEGER, /* 1.man , 2.woman*/
    idCard NUMERIC,
    phoneNumber NUMERIC,
    email VARCHAR(50),
    nation VARCHAR(50),
    race VARCHAR(50)
);

insert into person(first_name,last_name,birthday,sex,idCard,phoneNumber,email,nation,race)
VALUES('anan','seti','2510-10-10',1,3411400402914,0181469369,'anan.sati@gmail.com','ไทย','ไทย');

CREATE TABLE history_self(
id SERIAL PRIMARY KEY,
personHistoryId INTEGER not NULL,
optionhistoryCACheck INTEGER , /* 0. ไม่เป็น  1.เป็น*/
beastCheck INTEGER,
bCAYear INTEGER, /*ปีที่เป็นมะเร็งเต้านม*/
ิิิbothBreatCACheck INTEGER , /*ตรวจพบมเร็งเต้านมสองข้าง*/
ิbovalCheck INTEGER,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
bovalYear INTEGER,
ิbgutCheck INTEGER,
bgutYear INTEGER,
liverCheck INTEGER, /*มะเร็งตับอ่อน*/
ิbliverYear INTEGER, /*ปีที่เป็น*/
postgrandCheck INTEGER, /*มะเร็งต่อมลูกหมาก*/
bpostgrandyear INTEGER, /* ปีที่เป็น*/
skinCheck  INTEGER, /*มะเร็งผิวหนัง */
bskinyear INTEGER, /*ปีที่เป็น */
FOREIGN KEY(personHistoryId) REFERENCES person(id)
);

insert into history_self(
personHistoryId ,
optionhistoryCACheck ,
beastCheck ,
bCAYear, /*ปีที่เป็นมะเร็งเต้านม*/
ิิิbothBreatCACheck , /*ตรวจพบมเร็งเต้านมสองข้าง*/
ิbovalCheck ,/*มะเร็งรังไข่ * 0 ไม่พบ 1 พบ*/
bovalYear,
ิbgutCheck ,
bgutYear ,
liverCheck , /*มะเร็งตับอ่อน*/
ิbliverYear , /*ปีที่เป็น*/
postgrandCheck , /*มะเร็งต่อมลูกหมาก*/
bpostgrandyear , /* ปีที่เป็น*/
skinCheck  , /*มะเร็งผิวหนัง */
bskinyear  /*ปีที่เป็น */
)
VALUES(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1);
