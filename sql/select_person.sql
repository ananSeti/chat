--/home/anan/dev/chat/sql

select accountid ,first_name,last_name,birthday,sex,idcard,phonenumber,nation,race,created
from person p join a_user u on p.accountid = u.id;


