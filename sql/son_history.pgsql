select sonHistoryId,optionhistoryson,sonbreastcheck,sonbreatyear,sonliverCheck,sonliveryear,songutCheck,
songutyear,sonpostGrandCheck,sonpostGrandYear,sonskinCheck,sonskinyear,created
from son_history sh join a_user u on sh.accountid = u.id 
where  u.id = %s order by u.id DESC limit 1,(user_id,)


insert into son_history( sonHistoryId,optionhistoryson,sonbreastcheck,sonbreatyear,sonliverCheck,sonliveryear,songutCheck,
songutyear,sonpostGrandCheck,sonpostGrandYear,sonskinCheck,sonskinyear)
values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s),

