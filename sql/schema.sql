CREATE TABLE person(
    id  SERIAL PRIMARY KEY ,
    first_name TEXT not NULL,
    last_name TEXT, 
    birthday date,
    sex  INTEGER,

)