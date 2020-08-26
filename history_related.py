from flask import(
    Blueprint,flash,g,redirect,render_template,session,request,url_for
)
from werkzeug.exceptions import abort
from chat.db import get_db
from chat.chatclass import person

#ประวัติลูกชาย
def get_sonHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select sonhistoryid,optionhistoryson,sonbreastcheck,sonbreastyear,sonliverCheck,sonliveryear,songutCheck,'
      ' songutyear,sonpostGrandCheck,sonpostGrandYear,sonskinCheck,sonskinyear,created '
      ' from son_history sh join a_user u on sh.sonhistoryid = u.id '
      ' where  u.id = %s order by sonhistoryid DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.sonHistory(
        accountid = 0,
        optionhistoryson = 99 ,  # not select
        sonbreastcheck= 0,
        sonbreastyear= 0,
        sonliverCheck =0,
        sonliveryear =0,
        songutCheck =0,
        songutyear =0,
        sonpostGrandCheck =0,
        sonpostGrandYear =0,
        sonskinCheck=0,
        sonskinyear=0
      )
    else:
      p =person.sonHistory(
        accountid = infos[0][0],
        optionhistoryson = infos[0][1] ,  # not select
        sonbreastcheck= infos[0][2],
        sonbreastyear= infos[0][3],
        sonliverCheck =infos[0][4],
        sonliveryear =infos[0][5],
        songutCheck =infos[0][6],
        songutyear =infos[0][7],
        sonpostGrandCheck =infos[0][8],
        sonpostGrandYear =infos[0][9],
        sonskinCheck=infos[0][10],
        sonskinyear=infos[0][11]
      )
    return p
def insert_sonHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.sonHistory(
        accountid= int(user_id),
        optionhistoryson = int(request.form.get('optionhistoryson')) if not (request.form.get('optionhistoryson'))==None else 99,
        sonbreastcheck= int(request.form.get('sonbreastcheck')) if not (request.form.get('sonbreastcheck'))==None  else 0,
        sonbreastyear= int(request.form.get('sonbreastyear')) if not (request.form.get('sonbreastyear'))==''  else 0,
        sonliverCheck =int(request.form.get('sonliverCheck')) if not (request.form.get('sonliverCheck'))==None  else 0,
        sonliveryear =int(request.form.get('sonliveryear')) if not (request.form.get('sonliveryear'))=='' else 0,
        songutCheck = int(request.form.get('songutCheck')) if not (request.form.get('songutCheck'))==None  else 0,
        songutyear =int(request.form.get('songutyear')) if not (request.form.get('songutyear'))==''  else 0,
        sonpostGrandCheck = int(request.form.get('sonpostGrandCheck')) if not (request.form.get('sonpostGrandCheck'))==None  else 0,
        sonpostGrandYear =int(request.form.get('sonpostGrandrYear')) if not (request.form.get('sonpostGrandrYear'))=='' else 0,
        sonskinCheck= int(request.form.get('sonskinCheck')) if not (request.form.get('sonskinCheck'))==None  else 0,
        sonskinyear=int(request.form.get('sonskinyear')) if not (request.form.get('sonskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into son_history(sonhistoryid,optionhistoryson,sonbreastcheck,sonbreastyear,sonlivercheck,sonliveryear, '
       ' songutcheck,songutyear,sonpostgrandcheck,sonpostgrandyear,sonskincheck,sonskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistoryson,p.sonbreastcheck,p.sonbreastyear,p.sonliverCheck,p.sonliveryear
       ,p.songutCheck,p.songutyear,p.sonpostGrandCheck,p.sonpostGrandYear,p.sonskinCheck,p.sonskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติลูกชาย เรียบร้อย...' 
                flash(error)
                return p  
#ประวัติลูกสาว
def get_daugtherHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select daughterhistoryid,optionhistorydaughter,daughterbreastcheck ,daughterbreastyear ,daughterlivercheck ,daughterliveryear ,daughtergutcheck ,'
      ' daughtergutyear ,daughterpostgrandcheck ,daughterpostgrandyear ,daughterskincheck  ,daughterskinyear ,created '
      ' from daughter_history sh join a_user u on sh.daughterhistoryid = u.id '
      ' where  u.id = %s order by daughterhistoryid DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.daughterHistory(
        accountid = 0,
        optionhistorydaughter = 99 ,  # not select
        daughterbreastCheck= 0,
        daughterbreastyear= 0,
        daughterliverCheck =0,
        daughterliveryear =0,
        daughtergutCheck =0,
        daughtergutyear =0,
        daughterpostGrandCheck =0,
        daughterpostGrandyear =0,
        daughterskinCheck=0,
        daughterskinyear=0
        )
    else:
      p = person.daughterHistory(
        accountid = infos[0][0],
        optionhistorydaughter = infos[0][1] ,  # not select
        daughterbreastCheck= infos[0][2],
        daughterbreastyear= infos[0][3],
        daughterliverCheck =infos[0][4],
        daughterliveryear =infos[0][5],
        daughtergutCheck =infos[0][6],
        daughtergutyear =infos[0][7],
        daughterpostGrandCheck =infos[0][8],
        daughterpostGrandyear =infos[0][9],
        daughterskinCheck=infos[0][10],
        daughterskinyear=infos[0][11]
        )
    return p
def insert_daugterHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.daughterHistory(
        accountid= int(user_id),
        optionhistorydaughter = int(request.form.get('optionhistorydaughter')) if not (request.form.get('optionhistorydaughter'))==None else 99,
        daughterbreastCheck= int(request.form.get('daughterbreastCheck')) if not (request.form.get('daughterbreastCheck'))==None  else 0,
        daughterbreastyear= int(request.form.get('daughterbreastyear')) if not (request.form.get('daughterbreastyear'))==''  else 0,
        daughterliverCheck =int(request.form.get('daughterliverCheck')) if not (request.form.get('daughterliverCheck'))==None  else 0,
        daughterliveryear =int(request.form.get('daughterliveryear')) if not (request.form.get('daughterliveryear'))=='' else 0,
        daughtergutCheck = int(request.form.get('daughtergutCheck')) if not (request.form.get('daughtergutCheck'))==None  else 0,
        daughtergutyear =int(request.form.get('daughtergutyear')) if not (request.form.get('daughtergutyear'))==''  else 0,
        daughterpostGrandCheck = int(request.form.get('daughterpostGrandCheck')) if not (request.form.get('daughterpostGrandCheck'))==None  else 0,
        daughterpostGrandyear =int(request.form.get('daughterpostGrandyear')) if not (request.form.get('daughterpostGrandrYear'))=='' else 0,
        daughterskinCheck= int(request.form.get('daughterskinCheck')) if not (request.form.get('daughterskinCheck'))==None  else 0,
        daughterskinyear=int(request.form.get('daughterskinyear')) if not (request.form.get('daughterskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into daughter_history(daughterhistoryid,optionhistorydaughter,daughterbreastcheck ,daughterbreastyear ,daughterlivercheck ,daughterliveryear ,daughtergutcheck ,'
       ' daughtergutyear ,daughterpostgrandcheck ,daughterpostgrandyear ,daughterskincheck  ,daughterskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorydaughter,p.daughterbreastCheck,p.daughterbreastyear,p.daughterliverCheck,p.daughterliveryear,p.daughtergutCheck,
         p.daughtergutyear,p.daughterpostGrandCheck,p.daughterpostGrandyear,p.daughterskinCheck,p.daughterskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติลูกสาว เรียบร้อย...' 
                flash(error)
                return p 
#ประวัติพ่อ
def get_fatherHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select fatherhistoryid,optionhistoryfather,fatherbreastcheck ,fatherbreastyear ,fatherlivercheck ,fatherliveryear ,fathergutcheck ,'
      ' fathergutyear ,fatherpostgrandcheck ,fatherpostgrandyear ,fatherskincheck  ,fatherskinyear ,created '
      ' from father_history sh join a_user u on sh.fatherhistoryid = u.id '
      ' where  u.id = %s order by fatherhistoryid DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.fatherHistory(
        accountid = 0,
        optionhistoryfather = 99 ,  # not select
        fatherbreastCheck= 0,
        fatherbreastyear= 0,
        fatherliverCheck =0,
        fatherliveryear =0,
        fathergutCheck =0,
        fathergutyear =0,
        fatherpostGrandCheck =0,
        fatherpostGrandyear =0,
        fatherskinCheck=0,
        fatherskinyear=0
        )
    else:
      p = person.fatherHistory(
        accountid = infos[0][0],
        optionhistoryfather = infos[0][1] ,  # not select
        fatherbreastCheck= infos[0][2],
        fatherbreastyear= infos[0][3],
        fatherliverCheck =infos[0][4],
        fatherliveryear =infos[0][5],
        fathergutCheck =infos[0][6],
        fathergutyear =infos[0][7],
        fatherpostGrandCheck =infos[0][8],
        fatherpostGrandyear =infos[0][9],
        fatherskinCheck=infos[0][10],
        fatherskinyear=infos[0][11]
        )
    return p
def insert_fatherHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.fatherHistory(
        accountid= int(user_id),
        optionhistoryfather = int(request.form.get('optionhistoryfather')) if not (request.form.get('optionhistoryfather'))==None else 99,
        fatherbreastCheck= int(request.form.get('fatherbreatCheck')) if not (request.form.get('fatherbreatCheck'))==None  else 0,
        fatherbreastyear= int(request.form.get('fatherbreastyear')) if not (request.form.get('fatherbreastyear'))==''  else 0,
        fatherliverCheck =int(request.form.get('fatherliverCheck')) if not (request.form.get('fatherliverCheck'))==None  else 0,
        fatherliveryear =int(request.form.get('fatherliveryear')) if not (request.form.get('fatherliveryear'))=='' else 0,
        fathergutCheck = int(request.form.get('fathergutCheck')) if not (request.form.get('fathergutCheck'))==None  else 0,
        fathergutyear =int(request.form.get('fathergutyear')) if not (request.form.get('fathergutyear'))==''  else 0,
        fatherpostGrandCheck = int(request.form.get('fatherpostGrandCheck')) if not (request.form.get('fatherpostGrandCheck'))==None  else 0,
        fatherpostGrandyear =int(request.form.get('fartherpostGrandyear')) if not (request.form.get('fartherpostGrandyear'))=='' else 0,
        fatherskinCheck= int(request.form.get('fatherskinCheck')) if not (request.form.get('fatherskinCheck'))==None  else 0,
        fatherskinyear=int(request.form.get('fatherskinyear')) if not (request.form.get('fatherskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into father_history(fatherhistoryid,optionhistoryfather,fatherbreastcheck ,fatherbreastyear ,fatherlivercheck ,fatherliveryear ,fathergutcheck ,'
       ' fathergutyear ,fatherpostgrandcheck ,fatherpostgrandyear ,fatherskincheck  ,fatherskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistoryfather,p.fatherbreatCheck,p.fatherbreastyear,p.fatherliverCheck,p.fatherliveryear,p.fathergutCheck,
         p.fathergutyear,p.fatherpostGrandCheck,p.fatherpostGrandyear,p.fatherskinCheck,p.fatherskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติพ่อ เรียบร้อย...' 
                flash(error)
                return p 