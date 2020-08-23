select p.first_name,
       h.optionhistorycacheck 

from person p
INNER JOIN history_self h
ON h.personhistoryid = p.id;
