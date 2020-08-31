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
      ' songutyear,sonpostGrandCheck,sonpostGrandYear,sonskinCheck,sonskinyear,created ,sh.id'
      ' from son_history sh join a_user u on sh.sonhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
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
      ' daughtergutyear ,daughterpostgrandcheck ,daughterpostgrandyear ,daughterskincheck  ,daughterskinyear ,created ,sh.id'
      ' from daughter_history sh join a_user u on sh.daughterhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
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
      ' fathergutyear ,fatherpostgrandcheck ,fatherpostgrandyear ,fatherskincheck  ,fatherskinyear ,created,sh.id '
      ' from father_history sh join a_user u on sh.fatherhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
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
        fatherpostGrandyear =int(request.form.get('fatherpostGrandyear')) if not (request.form.get('fatherpostGrandyear'))=='' else 0,
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
#ประวัติแม่
def get_motherrHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select motherhistoryid,optionhistorymother,motherbreastcheck ,motherbreastyear ,motherlivercheck ,motherliveryear ,mothergutcheck ,'
      ' mothergutyear ,motherpostgrandcheck ,motherpostgrandyear ,motherskincheck  ,motherskinyear ,created ,sh.id'
      ' from mother_history sh join a_user u on sh.motherhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.motherHistory(
        accountid = 0,
        optionhistorymother = 99 ,  # not select
        motherbreastCheck= 0,
        motherbreastyear= 0,
        motherliverCheck =0,
        motherliveryear =0,
        mothergutCheck =0,
        mothergutyear =0,
        motherpostGrandCheck =0,
        motherpostGrandyear =0,
        motherskinCheck=0,
        motherskinyear=0
        )
    else:
      p = person.motherHistory(
        accountid = infos[0][0],
        optionhistorymother = infos[0][1] ,  # not select
        motherbreastCheck= infos[0][2],
        motherbreastyear= infos[0][3],
        motherliverCheck =infos[0][4],
        motherliveryear =infos[0][5],
        mothergutCheck =infos[0][6],
        mothergutyear =infos[0][7],
        motherpostGrandCheck =infos[0][8],
        motherpostGrandyear =infos[0][9],
        motherskinCheck=infos[0][10],
        motherskinyear=infos[0][11]
        )
    return p
def insert_motherHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.motherHistory(
        accountid= int(user_id),
        optionhistorymother = int(request.form.get('optionhistorymother')) if not (request.form.get('optionhistorymother'))==None else 99,
        motherbreastCheck= int(request.form.get('motherbreastCheck')) if not (request.form.get('motherbreastCheck'))==None  else 0,
        motherbreastyear= int(request.form.get('motherbreastyear')) if not (request.form.get('motherbreastyear'))==None  else 0,
        motherliverCheck =int(request.form.get('motherliverCheck')) if not (request.form.get('motherliverCheck'))==None  else 0,
        motherliveryear =int(request.form.get('motherliveryear')) if not (request.form.get('motherliveryear'))=='' else 0,
        mothergutCheck = int(request.form.get('mothergutCheck')) if not (request.form.get('mothergutCheck'))==None  else 0,
        mothergutyear =int(request.form.get('mothergutyear')) if not (request.form.get('mothergutyear'))==''  else 0,
        motherpostGrandCheck = int(request.form.get('motherpostGrandCheck')) if not (request.form.get('motherpostGrandCheck'))==None  else 0,
        motherpostGrandyear =int(request.form.get('motherpostGrandyear')) if not (request.form.get('motherpostGrandyear'))=='' else 0,
        motherskinCheck= int(request.form.get('motherskinCheck')) if not (request.form.get('motherskinCheck'))==None  else 0,
        motherskinyear=int(request.form.get('motherskinyear')) if not (request.form.get('motherskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into mother_history(motherhistoryid,optionhistorymother,motherbreastcheck ,motherbreastyear ,motherlivercheck ,motherliveryear ,mothergutcheck ,'
       ' mothergutyear ,motherpostgrandcheck ,motherpostgrandyear ,motherskincheck  ,motherskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorymother,p.motherbreastCheck,p.motherbreastyear,p.motherliverCheck,p.motherliveryear,p.mothergutCheck,
         p.mothergutyear,p.motherpostGrandCheck,p.motherpostGrandyear,p.motherskinCheck,p.motherskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติแม่ เรียบร้อย...' 
                flash(error)
                return p 
 #ประวัติน้องชาย

#ประวัติน้องชาย
def get_brotherHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select brotherhistoryid,optionhistorybrother,brotherbreastcheck ,brotherbreastyear ,brotherlivercheck ,brotherliveryear ,brothergutcheck ,'
      ' brothergutyear ,brotherpostgrandcheck ,brotherpostgrandyear ,brotherskincheck  ,brotherskinyear ,created ,sh.id'
      ' from brother_history sh join a_user u on sh.brotherhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.brotherHistory(
        accountid = 0,
        optionhistorybrother = 99 ,  # not select
        brotherbreastCheck= 0,
        brotherbreastyear= 0,
        brotherliverCheck =0,
        brotherliveryear =0,
        brothergutCheck =0,
        brothergutyear =0,
        brotherpostGrandCheck =0,
        brotherpostGrandyear =0,
        brotherskinCheck=0,
        brotherskinyear=0
        )
    else:
      p = person.brotherHistory(
        accountid = infos[0][0],
        optionhistorybrother = infos[0][1] ,  # not select
        brotherbreastCheck= infos[0][2],
        brotherbreastyear= infos[0][3],
        brotherliverCheck =infos[0][4],
        brotherliveryear =infos[0][5],
        brothergutCheck =infos[0][6],
        brothergutyear =infos[0][7],
        brotherpostGrandCheck =infos[0][8],
        brotherpostGrandyear =infos[0][9],
        brotherskinCheck=infos[0][10],
        brotherskinyear=infos[0][11]
        )
    return p
def insert_brotherHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.brotherHistory(
        accountid= int(user_id),
        optionhistorybrother = int(request.form.get('optionhistorybrother')) if not (request.form.get('optionhistorybrother'))==None else 0,
        brotherbreastCheck= int(request.form.get('brotherbreastCheck')) if not (request.form.get('brotherbreastCheck'))==None  else 0,
        brotherbreastyear= int(request.form.get('brotherbreastyear')) if not (request.form.get('brotherbreastyear'))==''  else 0,
        brotherliverCheck =int(request.form.get('brotherliverCheck')) if not (request.form.get('brotherliverCheck'))==None  else 0,
        brotherliveryear =int(request.form.get('brotherliveryear')) if not (request.form.get('brotherliveryear'))=='' else 0,
        brothergutCheck = int(request.form.get('brothergutCheck')) if not (request.form.get('brothergutCheck'))==None else 0,
        brothergutyear =int(request.form.get('brothergutyear')) if not (request.form.get('brothergutyear'))==''  else 0,
        brotherpostGrandCheck = int(request.form.get('brotherpostGrandCheck')) if not (request.form.get('brotherpostGrandCheck'))==None  else 0,
        brotherpostGrandyear =int(request.form.get('brotherpostGrandyear')) if not (request.form.get('brotherpostGrandyear'))=='' else 0,
        brotherskinCheck= int(request.form.get('brotherskinCheck')) if not (request.form.get('brotherskinCheck'))==None else 0,
        brotherskinyear=int(request.form.get('brotherskinyear')) if not (request.form.get('brorskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into brother_history(brotherhistoryid,optionhistorybrother,brotherbreastcheck ,brotherbreastyear ,brotherlivercheck ,brotherliveryear ,brothergutcheck ,'
       ' brothergutyear ,brotherpostgrandcheck ,brotherpostgrandyear ,brotherskincheck  ,brotherskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorybrother,p.brotherbreastCheck,p.brotherbreastyear,p.brotherliverCheck,p.brotherliveryear,p.brothergutCheck,
         p.brothergutyear,p.brotherpostGrandCheck,p.brotherpostGrandyear,p.brotherskinCheck,p.brotherskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติน้องชาย เรียบร้อย...' 
                flash(error)
                return p
#ประวัติน้องสาว
def get_sisterHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select sisterhistoryid,optionhistorysister,sisterbreastcheck ,sisterbreastyear ,sisterlivercheck ,sisterliveryear ,sistergutcheck ,'
      ' sistergutyear ,sisterpostgrandcheck ,sisterpostgrandyear ,sisterskincheck  ,sisterskinyear ,created ,sh.id'
      ' from sister_history sh join a_user u on sh.sisterhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.sisterHistory(
        accountid = 0,
        optionhistorysister = 99 ,  # not select
        sisterbreastCheck= 0,
        sisterbreastyear= 0,
        sisterliverCheck =0,
        sisterliveryear =0,
        sistergutCheck =0,
        sistergutyear =0,
        sisterpostGrandCheck =0,
        sisterpostGrandyear =0,
        sisterskinCheck=0,
        sisterskinyear=0
        )
    else:
      p = person.sisterHistory(
        accountid = infos[0][0],
        optionhistorysister = infos[0][1] ,  # not select
        sisterbreastCheck= infos[0][2],
        sisterbreastyear= infos[0][3],
        sisterliverCheck =infos[0][4],
        sisterliveryear =infos[0][5],
        sistergutCheck =infos[0][6],
        sistergutyear =infos[0][7],
        sisterpostGrandCheck =infos[0][8],
        sisterpostGrandyear =infos[0][9],
        sisterskinCheck=infos[0][10],
        sisterskinyear=infos[0][11]
        )
    return p
def insert_sisterHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.sisterHistory(
        accountid= int(user_id),
        optionhistorysister = int(request.form.get('optionhistorysister')) if not (request.form.get('optionhistorysister'))==None else 0,
        sisterbreastCheck= int(request.form.get('sisterbreastCheck')) if not (request.form.get('sisterbreastCheck'))==None  else 0,
        sisterbreastyear= int(request.form.get('sisterbreastyear')) if not (request.form.get('sisterbreastyear'))==None  else 0,
        sisterliverCheck =int(request.form.get('sisterliverCheck')) if not (request.form.get('sisterliverCheck'))==None  else 0,
        sisterliveryear =int(request.form.get('sisterliveryear')) if not (request.form.get('sisterliveryear'))=='' else 0,
        sistergutCheck = int(request.form.get('sistergutCheck')) if not (request.form.get('sistergutCheck'))==None  else 0,
        sistergutyear =int(request.form.get('sistergutyear')) if not (request.form.get('sistergutyear'))==''  else 0,
        sisterpostGrandCheck = int(request.form.get('sisterpostGrandCheck')) if not (request.form.get('sisterpostGrandCheck'))==None  else 0,
        sisterpostGrandyear =int(request.form.get('sisterpostGrandyear')) if not (request.form.get('sisterpostGrandyear'))=='' else 0,
        sisterskinCheck= int(request.form.get('sisterskinCheck')) if not (request.form.get('sisterskinCheck'))==None  else 0,
        sisterskinyear=int(request.form.get('sisterskinyear')) if not (request.form.get('sisterskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into sister_history(sisterhistoryid,optionhistorysister,sisterbreastcheck ,sisterbreastyear ,sisterlivercheck ,sisterliveryear ,sistergutcheck ,'
       ' sistergutyear ,sisterpostgrandcheck ,sisterpostgrandyear ,sisterskincheck  ,sisterskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorysister,p.sisterbreastCheck,p.sisterbreastyear,p.sisterliverCheck,p.sisterliveryear,p.sistergutCheck,
         p.sistergutyear,p.sisterpostGrandCheck,p.sisterpostGrandyear,p.sisterskinCheck,p.sisterskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติน้องสาว  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติทวดชาย
def get_mangrandfaHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select mangrandfahistoryid,optionhistorymangrandfather,mangrandfabreastcheck ,mangrandfabreastyear ,mangrandfalivercheck ,mangrandfaliveryear ,mangrandfagutcheck ,'
      ' mangrandfagutyear ,mangrandfapostgrandcheck ,mangrandfapostgrandyear ,mangrandfaskincheck  ,mangrandfaskinyear ,created ,sh.id'
      ' from mangrandfa_history sh join a_user u on sh.mangrandfahistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.mangrandFaHistory(
        accountid = 0,
        optionhistorymangrandfather = 99 ,  # not select
        mangrandFabreastCheck= 0,
        mangrandFabreastyear= 0,
        mangrandFaliverCheck =0,
        mangrandFaliveryear =0,
        mangrandFagutCheck =0,
        mangrandFagutyear =0,
        mangrandFapostGrandCheck =0,
        mangrandFapostGrandyear =0,
        mangrandFaskinCheck=0,
        mangrandFaskinyear=0
        )
    else:
      p = person.mangrandFaHistory(
        accountid = infos[0][0],
        optionhistorymangrandfather = infos[0][1] ,  # not select
        mangrandFabreastCheck= infos[0][2],
        mangrandFabreastyear= infos[0][3],
        mangrandFaliverCheck =infos[0][4],
        mangrandFaliveryear =infos[0][5],
        mangrandFagutCheck =infos[0][6],
        mangrandFagutyear =infos[0][7],
        mangrandFapostGrandCheck =infos[0][8],
        mangrandFapostGrandyear =infos[0][9],
        mangrandFaskinCheck=infos[0][10],
        mangrandFaskinyear=infos[0][11]
        )
    return p
def insert_mangrandfaHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.mangrandFaHistory(
        accountid= int(user_id),
        optionhistorymangrandfather = int(request.form.get('optionhistorygrandfather')) if not (request.form.get('optionhistorygrandfather'))==None else 99,
        mangrandFabreastCheck= int(request.form.get('mangrandFabreastCheck')) if not (request.form.get('mangrandFabreastCheck'))==None  else 0,
        mangrandFabreastyear= int(request.form.get('mangrandFabreastyear')) if not (request.form.get('mangrandFabreastyear'))==None  else 0,
        mangrandFaliverCheck =int(request.form.get('mangrandFaliverCheck')) if not (request.form.get('mangrandFaliverCheck'))==None  else 0,
        mangrandFaliveryear =int(request.form.get('mangrandFaliveryear')) if not (request.form.get('mangrandFaliveryear'))=='' else 0,
        mangrandFagutCheck = int(request.form.get('mangrandFagutCheck')) if not (request.form.get('mangrandFagutCheck'))==None  else 0,
        mangrandFagutyear =int(request.form.get('mangrandFagutyear')) if not (request.form.get('mangrandFagutyear'))==''  else 0,
        mangrandFapostGrandCheck = int(request.form.get('mangrandFapostGrandCheck')) if not (request.form.get('mangrandFapostGrandCheck'))==None  else 0,
        mangrandFapostGrandyear =int(request.form.get('mangrandFapostGrandyear')) if not (request.form.get('mangrandFapostGrandyear'))=='' else 0,
        mangrandFaskinCheck= int(request.form.get('mangrandFaskinCheck')) if not (request.form.get('mangrandFaskinCheck'))==None  else 0,
        mangrandFaskinyear=int(request.form.get('mangrandFaskinyear')) if not (request.form.get('mangrandFaskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into mangrandfa_history(mangrandfahistoryid,optionhistorymangrandfather,mangrandfabreastcheck ,mangrandfabreastyear ,mangrandfalivercheck ,mangrandfaliveryear ,mangrandfagutcheck ,'
       ' mangrandfagutyear ,mangrandfapostgrandcheck ,mangrandfapostgrandyear ,mangrandfaskincheck  ,mangrandfaskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorymangrandfather,p.mangrandFagutCheck,p.mangrandFabreastyear,p.mangrandFaliverCheck,p.mangrandFaliveryear,p.mangrandFagutCheck,
         p.mangrandFagutyear,p.mangrandFapostGrandCheck,p.mangrandFapostGrandyear,p.mangrandFaskinCheck,p.mangrandFaskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติทวดชาย  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติทวด หญิง
def get_womangrandMomHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select womangrandmomhistoryid,optionhistorywomangrandmother,womangrandmombreastcheck ,womangrandmombreastyear ,womangrandmomlivercheck ,womangrandmomliveryear ,womangrandmomgutcheck ,'
      ' womangrandmomgutyear ,womangrandmompostgrandcheck ,womangrandmompostgrandyear ,womangrandmomskincheck  ,womangrandmomskinyear ,created ,sh.id'
      ' from womangrandmom_history sh join a_user u on sh.womangrandmomhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.womangranMomHistory(
        accountid = 0,
        optionhistorywomangrandmother = 99 ,  # not select
        womangrandMombreastCheck= 0,
        womangrandMombreastyear= 0,
        womangrandMomliverCheck =0,
        womangrandMomliveryear =0,
        womangrandMomgutCheck =0,
        womangrandMomgutyear =0,
        womangrandMompostGrandCheck =0,
        womangrandMompostGrandyear =0,
        womangrandMomskinCheck=0,
        womangrandMomskinyear=0
        )
    else:
      p = person.womangranMomHistory(
        accountid = infos[0][0],
        optionhistorywomangrandmother = infos[0][1] ,  # not select
        womangrandMombreastCheck= infos[0][2],
        womangrandMombreastyear= infos[0][3],
        womangrandMomliverCheck =infos[0][4],
        womangrandMomliveryear =infos[0][5],
        womangrandMomgutCheck =infos[0][6],
        womangrandMomgutyear =infos[0][7],
        womangrandMompostGrandCheck =infos[0][8],
        womangrandMompostGrandyear =infos[0][9],
        womangrandMomskinCheck=infos[0][10],
        womangrandMomskinyear=infos[0][11]
        )
    return p
def insert_womangrandMomHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.womangranMomHistory(
        accountid= int(user_id),
        optionhistorywomangrandmother = int(request.form.get('optionhistorywomangrandmother')) if not (request.form.get('optionhistorywomangrandmother'))=='' else 99,
        womangrandMombreastCheck= int(request.form.get('womangrandMombreastCheck')) if not (request.form.get('womangrandMombreastCheck'))==None  else 0,
        womangrandMombreastyear= int(request.form.get('womangrandMombreastyear')) if not (request.form.get('womangrandMombreastyear'))==None  else 0,
        womangrandMomliverCheck =int(request.form.get('womangrandMomliverCheck')) if not (request.form.get('womangrandMomliverCheck'))==None  else 0,
        womangrandMomliveryear =int(request.form.get('womangrandMomliveryear')) if not (request.form.get('womangrandMomliveryear'))=='' else 0,
        womangrandMomgutCheck = int(request.form.get('womangrandMomgutCheck')) if not (request.form.get('womangrandMomgutCheck'))==None  else 0,
        womangrandMomgutyear =int(request.form.get('womangrandMomgutyear')) if not (request.form.get('womangrandMomgutyear'))==''  else 0,
        womangrandMompostGrandCheck = int(request.form.get('womangrandMompostGrandCheck')) if not (request.form.get('womangrandMompostGrandCheck'))==None  else 0,
        womangrandMompostGrandyear =int(request.form.get('womangrandMompostGrandyear')) if not (request.form.get('womangrandMompostGrandyear'))=='' else 0,
        womangrandMomskinCheck= int(request.form.get('womangrandMomskinCheck')) if not (request.form.get('womangrandMomskinCheck'))==None  else 0,
        womangrandMomskinyear=int(request.form.get('womangrandMomskinyear')) if not (request.form.get('womangrandMomskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into womangrandmom_history(womangrandmomhistoryid,optionhistorywomangrandmother,womangrandmombreastcheck ,womangrandmombreastyear ,womangrandmomlivercheck ,womangrandmomliveryear ,womangrandmomgutcheck ,'
       ' womangrandmomgutyear ,womangrandmompostgrandcheck ,womangrandmompostgrandyear ,womangrandmomskincheck  ,womangrandmomskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorywomangrandmother,p.womangrandMombreastCheck,p.womangrandMombreastyear,p.womangrandMomliverCheck,p.womangrandMomliveryear,p.womangrandMomgutCheck,
         p.womangrandMomgutyear,p.womangrandMompostGrandCheck,p.womangrandMompostGrandyear,p.womangrandsMomskinCheck,p.womangrandMomskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติทวดหญิง  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติปู่
def get_grandFatherHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select grandfatherhistoryid,optionhistorygrandfather,grandfatherbreastcheck ,grandfatherbreastyear ,grandfatherlivercheck ,grandfatherliveryear ,grandfathergutcheck ,'
      ' grandfathergutyear ,grandfatherpostgrandcheck ,grandfatherpostgrandyear ,grandfatherskincheck  ,grandfatherskinyear ,created ,sh.id'
      ' from grandfather_history sh join a_user u on sh.grandfatherhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.grandFatherHistory(
        accountid = 0,
        optionhistorygrandfather = 99 ,  # not select
        grandFatherbreastCheck= 0,
        grandFatherbreastyear= 0,
        grandFatherliverCheck =0,
        grandFatherliveryear =0,
        grandFathergutCheck =0,
        grandFathergutyear =0,
        grandFatherpostGrandCheck =0,
        grandFatherpostGrandyear =0,
        grandFatherskinCheck=0,
        grandFatherskinyear=0
        )
    else:
      p = person.grandFatherHistory(
        accountid = infos[0][0],
        optionhistorygrandfather = infos[0][1] ,  # not select
        grandFatherbreastCheck= infos[0][2],
        grandFatherbreastyear= infos[0][3],
        grandFatherliverCheck =infos[0][4],
        grandFatherliveryear =infos[0][5],
        grandFathergutCheck =infos[0][6],
        grandFathergutyear =infos[0][7],
        grandFatherpostGrandCheck =infos[0][8],
        grandFatherpostGrandyear =infos[0][9],
        grandFatherskinCheck=infos[0][10],
        grandFatherskinyear=infos[0][11]
        )
    return p
def insert_grandFatherHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.grandFatherHistory(
        accountid= int(user_id),
        optionhistorygrandfather = int(request.form.get('optionhistorygrandfather')) if not (request.form.get('optionhistorygrandfather'))=='' else 99,
        grandFatherbreastCheck= int(request.form.get('grandFatherbreastCheck')) if not (request.form.get('grandFatherbreastCheck'))==None  else 0,
        grandFatherbreastyear= int(request.form.get('grandFatherbreastyear')) if not (request.form.get('grandFatherbreastyear'))==None  else 0,
        grandFatherliverCheck =int(request.form.get('grandFatherliverCheck')) if not (request.form.get('grandFatherliverCheck'))==None  else 0,
        grandFatherliveryear =int(request.form.get('grandFatherliveryear')) if not (request.form.get('grandFatherliveryear'))=='' else 0,
        grandFathergutCheck = int(request.form.get('grandFathergutCheck')) if not (request.form.get('grandFathergutCheck'))==None  else 0,
        grandFathergutyear =int(request.form.get('grandFathergutyear')) if not (request.form.get('grandFathergutyear'))==''  else 0,
        grandFatherpostGrandCheck = int(request.form.get('grandFatherpostGrandCheck')) if not (request.form.get('grandFatherpostGrandCheck'))==None  else 0,
        grandFatherpostGrandyear =int(request.form.get('grandFatherpostGrandyear')) if not (request.form.get('grandFatherpostGrandyear'))=='' else 0,
        grandFatherskinCheck= int(request.form.get('grandFatherskinCheck')) if not (request.form.get('grandFatherskinCheck'))==None  else 0,
        grandFatherskinyear=int(request.form.get('grandFatherskinyear')) if not (request.form.get('grandFatherskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into grandfather_history(grandfatherhistoryid,optionhistorygrandfather,grandfatherbreastcheck ,grandfatherbreastyear ,grandfatherlivercheck ,grandfatherliveryear ,grandfathergutcheck ,'
       ' grandfathergutyear ,grandfatherpostgrandcheck ,grandfatherpostgrandyear ,grandfatherskincheck  ,grandfatherskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorygrandfather,p.grandFatherbreastCheck,p.grandFatherbreastyear,p.grandFartherliverCheck,p.grandFatherliveryear,p.grandFathergutCheck,
         p.grandFathergutyear,p.grandFatherpostgrandCheck,p.grandFatherpostGrandyear,p.grandFatherskinCheck,p.grandFatherskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติปู่  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติย่า
def get_grandMomHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select grandmomhistoryid,optionhistorygrandmother,grandmombreastcheck ,grandmombreastyear ,grandmomlivercheck ,grandmomliveryear ,grandmomgutcheck ,'
      ' grandmomgutyear ,grandmompostgrandcheck ,grandmompostgrandyear ,grandmomskincheck  ,grandmomskinyear ,created ,sh.id'
      ' from grandmom_history sh join a_user u on sh.grandmomhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.grandMomHistory(
        accountid = 0,
        optionhistorygrandmother = 99 ,  # not select
        grandMombreastCheck= 0,
        grandMombreastyear= 0,
        grandMomliverCheck =0,
        grandMomliveryear =0,
        grandMomgutCheck =0,
        grandMomgutyear =0,
        grandMompostGrandCheck =0,
        grandMompostGrandyear =0,
        grandMomskinCheck=0,
        grandMomskinyear=0
        )
    else:
      p = person.grandMomHistory(
        accountid = infos[0][0],
        optionhistorygrandmother = infos[0][1] ,  # not select
        grandMombreastCheck= infos[0][2],
        grandMombreastyear= infos[0][3],
        grandMomliverCheck =infos[0][4],
        grandMomliveryear =infos[0][5],
        grandMomgutCheck =infos[0][6],
        grandMomgutyear =infos[0][7],
        grandMompostGrandCheck =infos[0][8],
        grandMompostGrandyear =infos[0][9],
        grandMomskinCheck=infos[0][10],
        grandMomskinyear=infos[0][11]
        )
    return p
def insert_grandMomHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.grandMomHistory(
        accountid= int(user_id),
        optionhistorygrandmother = int(request.form.get('optionhistorygrandmother')) if not (request.form.get('optionhistorygrandmother'))==None else 99,
        grandMombreastCheck= int(request.form.get('grandMombreastCheck')) if not (request.form.get('grandMombreastCheck'))==None  else 0,
        grandMombreastyear= int(request.form.get('grandMombreastyear')) if not (request.form.get('grandMombreastyear'))==None  else 0,
        grandMomliverCheck =int(request.form.get('grandMomliverCheck')) if not (request.form.get('grandMomliverCheck'))==None  else 0,
        grandMomliveryear =int(request.form.get('grandMomliveryear')) if not (request.form.get('grandMomliveryear'))=='' else 0,
        grandMomgutCheck = int(request.form.get('grandMomgutCheck')) if not (request.form.get('grandMomgutCheck'))==None  else 0,
        grandMomgutyear =int(request.form.get('grandMomgutyear')) if not (request.form.get('grandMomgutyear'))==''  else 0,
        grandMompostGrandCheck = int(request.form.get('grandMompostGrandCheck')) if not (request.form.get('grandMompostGrandCheck'))==None  else 0,
        grandMompostGrandyear =int(request.form.get('grandMompostGrandyear')) if not (request.form.get('grandMompostGrandyear'))=='' else 0,
        grandMomskinCheck= int(request.form.get('grandMomskinCheck')) if not (request.form.get('grandMomskinCheck'))==None  else 0,
        grandMomskinyear=int(request.form.get('grandMomskinyear')) if not (request.form.get('grandMomskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into grandmom_history(grandmomhistoryid,optionhistorygrandmother,grandmombreastcheck ,grandmombreastyear ,grandmomlivercheck ,grandmomliveryear ,grandmomgutcheck ,'
       ' grandmomgutyear ,grandmompostgrandcheck ,grandmompostgrandyear ,grandmomskincheck  ,grandmomskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorygrandmother,p.grandMombreastCheck,p.grandMombreastyear,p.grandMomliverCheck,p.grandMomliveryear,p.grandMomgutCheck,
         p.grandMomgutyear,p.grandMompostGrandCheck,p.grandMompostGrandyear,p.grandMomskinCheck,p.grandMomskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติย่า  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติตา
def get_fatherOfMomHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select fatherofmomhistoryid,optionhistoryfathermom,fatherofmombreastcheck ,fatherofmombreastyear ,fatherofmomlivercheck ,fatherofmomliveryear ,fatherofmomgutcheck ,'
      ' fatherofmomgutyear ,fatherofmompostgrandcheck ,fatherofmompostgrandyear ,fatherofmomskincheck  ,fatherofmomskinyear ,created ,sh.id'
      ' from fatherofmom_history sh join a_user u on sh.fatherofmomhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.fatherOfMomHistory(
        accountid = 0,
        optionhistoryfathermom = 99 ,  # not select
        fatherOfMombreastCheck= 0,
        fatherOfMombreastyear= 0,
        fatherOfMomliverCheck =0,
        fatherOfMomliveryear =0,
        fatherOfMomgutCheck =0,
        fatherOfMomgutyear =0,
        fatherOfMompostGrandCheck =0,
        fatherOfMompostGrandyear =0,
        fatherOfMomskinCheck=0,
        fatherOfMomskinyear=0
        )
    else:
      p = person.fatherOfMomHistory(
        accountid = infos[0][0],
        optionhistoryfathermom = infos[0][1] ,  # not select
        fatherOfMombreastCheck= infos[0][2],
        fatherOfMombreastyear= infos[0][3],
        fatherOfMomliverCheck =infos[0][4],
        fatherOfMomliveryear =infos[0][5],
        fatherOfMomgutCheck =infos[0][6],
        fatherOfMomgutyear =infos[0][7],
        fatherOfMompostGrandCheck =infos[0][8],
        fatherOfMompostGrandyear =infos[0][9],
        fatherOfMomskinCheck=infos[0][10],
        fatherOfMomskinyear=infos[0][11]
        )
    return p
def insert_fatherOfMomHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.fatherOfMomHistory(
        accountid= int(user_id),
        optionhistoryfathermom = int(request.form.get('optionhistoryfathermom')) if not (request.form.get('optionhistoryfathermom'))=='' else 99,
        fatherOfMombreastCheck= int(request.form.get('fatherOfMombreastCheck')) if not (request.form.get('fatherOfMombreastCheck'))==None  else 0,
        fatherOfMombreastyear= int(request.form.get('fatherOfMombreastyear')) if not (request.form.get('fatherOfMombreastyear'))==None  else 0,
        fatherOfMomliverCheck =int(request.form.get('fatherOfMomliverCheck')) if not (request.form.get('fatherOfMomliverCheck'))==None  else 0,
        fatherOfMomliveryear =int(request.form.get('fatherOfMomliveryear')) if not (request.form.get('fatherOfMomliveryear'))=='' else 0,
        fatherOfMomgutCheck = int(request.form.get('fatherOfMomgutCheck')) if not (request.form.get('fatherOfMomgutCheck'))==None  else 0,
        fatherOfMomgutyear =int(request.form.get('fatherOfMomgutyear')) if not (request.form.get('fatherOfMomgutyear'))==''  else 0,
        fatherOfMompostGrandCheck = int(request.form.get('fatherOfMompostGrandCheck')) if not (request.form.get('fatherOfMompostGrandCheck'))==None  else 0,
        fatherOfMompostGrandyear =int(request.form.get('fatherOfMompostGrandyear')) if not (request.form.get('fatherOfMompostGrandyear'))=='' else 0,
        fatherOfMomskinCheck= int(request.form.get('fatherOfMomskinCheck')) if not (request.form.get('fatherOfMomskinCheck'))==None  else 0,
        fatherOfMomskinyear=int(request.form.get('fatherOfMomskinyear')) if not (request.form.get('fatherOfMomskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into fatherofmom_history(fatherofmomhistoryid,optionhistoryfathermom,fatherofmombreastcheck ,fatherofmombreastyear ,fatherofmomlivercheck ,fatherofmomliveryear ,fatherofmomgutcheck ,'
       ' fatherofmomgutyear ,fatherofmompostgrandcheck ,fatherofmompostgrandyear ,fatherofmomskincheck  ,fatherofmomskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistoryfathermom,p.fatherOfMombreastCheck,p.fatherOfMombreastyear,p.fatherOfMomliverCheck,p.fatherOfMomliveryear,p.fatherOfMomgutCheck,
         p.fatherOfMomgutyear,p.fatherOfMompostGrandCheck,p.fatherOfMompostGrandyear,p.fatherOfMomskinCheck,p.fatherOfMomskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติตา  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติยาย
def get_motherOfMomHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select motherofmomhistoryid,optionhistorymothermom,motherofmombreastcheck ,motherofmombreastyear ,motherofmomlivercheck ,motherofmomliveryear ,motherofmomgutcheck ,'
      ' motherofmomgutyear ,motherofmompostgrandcheck ,motherofmompostgrandyear ,motherofmomskincheck  ,motherofmomskinyear ,created ,sh.id'
      ' from motherofmom_history sh join a_user u on sh.motherofmomhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.motherOfMomHistory(
        accountid = 0,
        optionhistorymothermom = 99 ,  # not select
        motherOfMombreastCheck= 0,
        motherOfMombreastyear= 0,
        motherOfMomliverCheck =0,
        motherOfMomliveryear =0,
        motherOfMomgutCheck =0,
        motherOfMomgutyear =0,
        motherOfMompostGrandCheck =0,
        motherOfMompostGrandyear =0,
        motherOfMomskinCheck=0,
        motherOfMomskinyear=0
        )
    else:
      p = person.motherOfMomHistory(
        accountid = infos[0][0],
        optionhistorymothermom = infos[0][1] ,  # not select
        motherOfMombreastCheck= infos[0][2],
        motherOfMombreastyear= infos[0][3],
        motherOfMomliverCheck =infos[0][4],
        motherOfMomliveryear =infos[0][5],
        motherOfMomgutCheck =infos[0][6],
        motherOfMomgutyear =infos[0][7],
        motherOfMompostGrandCheck =infos[0][8],
        motherOfMompostGrandyear =infos[0][9],
        motherOfMomskinCheck=infos[0][10],
        motherOfMomskinyear=infos[0][11]
        )
    return p
def insert_motherOfMomHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.motherOfMomHistory(
        accountid= int(user_id),
        optionhistorymothermom = int(request.form.get('optionhistorymothermom')) if not (request.form.get('optionhistorymothermom'))=='' else 99,
        motherOfMombreastCheck= int(request.form.get('motherOfMombreastCheck')) if not (request.form.get('motherOfMombreastCheck'))==None  else 0,
        motherOfMombreastyear= int(request.form.get('motherOfMombreastyear')) if not (request.form.get('motherOfMombreastyear'))==None  else 0,
        motherOfMomliverCheck =int(request.form.get('motherOfMomliverCheck')) if not (request.form.get('motherOfMomliverCheck'))==None  else 0,
        motherOfMomliveryear =int(request.form.get('motherOfMomliveryear')) if not (request.form.get('motherOfMomliveryear'))=='' else 0,
        motherOfMomgutCheck = int(request.form.get('motherOfMomgutCheck')) if not (request.form.get('motherOfMomgutCheck'))==None  else 0,
        motherOfMomgutyear =int(request.form.get('motherOfMomgutyear')) if not (request.form.get('motherOfMomgutyear'))==''  else 0,
        motherOfMompostGrandCheck = int(request.form.get('motherOfMompostGrandCheck')) if not (request.form.get('motherOfMompostGrandCheck'))==None  else 0,
        motherOfMompostGrandyear =int(request.form.get('motherOfMompostGrandyear')) if not (request.form.get('motherOfMompostGrandyear'))=='' else 0,
        motherOfMomskinCheck= int(request.form.get('motherOfMomskinCheck')) if not (request.form.get('motherOfMomskinCheck'))==None  else 0,
        motherOfMomskinyear=int(request.form.get('motherOfMomskinyear')) if not (request.form.get('motherOfMomskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into motherofmom_history(motherofmomhistoryid,optionhistorymothermom,motherofmombreastcheck ,motherofmombreastyear ,motherofmomlivercheck ,motherofmomliveryear ,motherofmomgutcheck ,'
       ' motherofmomgutyear ,motherofmompostgrandcheck ,motherofmompostgrandyear ,motherofmomskincheck  ,motherofmomskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorymothermom,p.motherOfMombreastCheck,p.motherOfMombreastyear,p.motherOfMomliverCheck,p.motherOfMomliveryear,p.motherOfMomgutCheck,
         p.motherOfMomgutyear,p.motherOfMompostGrandCheck,p.motherOfMompostGrandyear,p.motherOfMomskinCheck,p.motherOfMomskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติยาย  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติลุง
def get_bigUncleHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select bigunclehistoryid,optionhistorybiguncle,bigunclebreastcheck ,bigunclebreastyear ,bigunclelivercheck ,biguncleliveryear ,bigunclegutcheck ,'
      ' bigunclegutyear ,bigunclepostgrandcheck ,bigunclepostgrandyear ,biguncleskincheck  ,biguncleskinyear ,created ,sh.id'
      ' from biguncle_history sh join a_user u on sh.bigunclehistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.bigUncleHistory(
        accountid = 0,
        optionhistorybiguncle = 99 ,  # not select
        bigunclebreastCheck= 0,
        bigunclebreastyear= 0,
        biguncleliverCheck =0,
        biguncleliveryear =0,
        bigunclegutCheck =0,
        bigunclegutyear =0,
        bigunclepostGrandCheck =0,
        bigunclepostGrandyear =0,
        biguncleskinCheck=0,
        biguncleskinyear=0
        )
    else:
      p = person.bigUncleHistory(
        accountid = infos[0][0],
        optionhistorybiguncle = infos[0][1] ,  # not select
        bigunclebreastCheck= infos[0][2],
        bigunclebreastyear= infos[0][3],
        biguncleliverCheck =infos[0][4],
        biguncleliveryear =infos[0][5],
        bigunclegutCheck =infos[0][6],
        bigunclegutyear =infos[0][7],
        bigunclepostGrandCheck =infos[0][8],
        bigunclepostGrandyear =infos[0][9],
        biguncleskinCheck=infos[0][10],
        biguncleskinyear=infos[0][11]
        )
    return p
def insert_bigUncleHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.bigUncleHistory(
        accountid= int(user_id),
        optionhistorybiguncle = int(request.form.get('optionhistorybiguncle')) if not (request.form.get('optionhistorybiguncle'))=='' else 99,
        bigunclebreastCheck= int(request.form.get('bigunclebreastCheck')) if not (request.form.get('bigunclebreastCheck'))==None  else 0,
        bigunclebreastyear= int(request.form.get('bigunclebreastyear')) if not (request.form.get('bigunclebreastyear'))==None  else 0,
        biguncleliverCheck =int(request.form.get('biguncleliverCheck')) if not (request.form.get('biguncleliverCheck'))==None  else 0,
        biguncleliveryear =int(request.form.get('biguncleliveryear')) if not (request.form.get('biguncleliveryear'))=='' else 0,
        bigunclegutCheck = int(request.form.get('bigunclegutCheck')) if not (request.form.get('bigunclegutCheck'))==None  else 0,
        bigunclegutyear =int(request.form.get('bigunclegutyear')) if not (request.form.get('bigunclegutyear'))==''  else 0,
        bigunclepostGrandCheck = int(request.form.get('bigunclepostGrandCheck')) if not (request.form.get('bigunclepostGrandCheck'))==None  else 0,
        bigunclepostGrandyear =int(request.form.get('bigunclepostGrandyear')) if not (request.form.get('bigunclepostGrandyear'))=='' else 0,
        biguncleskinCheck= int(request.form.get('biguncleskinCheck')) if not (request.form.get('biguncleskinCheck'))==None  else 0,
        biguncleskinyear=int(request.form.get('biguncleskinyear')) if not (request.form.get('biguncleskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into biguncle_history(bigunclehistoryid,optionhistorybiguncle,bigunclebreastcheck ,bigunclebreastyear ,bigunclelivercheck ,biguncleliveryear ,bigunclegutcheck ,'
       ' bigunclegutyear ,bigunclepostgrandcheck ,bigunclepostgrandyear ,biguncleskincheck  ,biguncleskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorybiguncle,p.bigunclebreastCheck,p.bigunclebreastyear,p.biguncleliverCheck,p.biguncleliveryear,p.bigunclegutCheck,
         p.bigunclegutyear,p.bigunclepostGrandCheck,p.bigunclepostGrandyear,p.biguncleskinCheck,p.biguncleskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติลุง  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติป้า
def get_bigAuntHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select bigaunthistoryid,optionhistorybigaunt,bigauntbreastcheck ,bigauntbreastyear ,bigauntlivercheck ,bigauntliveryear ,bigauntgutcheck ,'
      ' bigauntgutyear ,bigauntpostgrandcheck ,bigauntpostgrandyear ,bigauntskincheck  ,bigauntskinyear ,created ,sh.id'
      ' from bigaunt_history sh join a_user u on sh.bigaunthistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.bigAuntHistory(
        accountid = 0,
        optionhistorybigaunt = 99 ,  # not select
        bigauntbreastCheck= 0,
        bigauntbreastyear= 0,
        bigauntliverCheck =0,
        bigauntliveryear =0,
        bigauntgutCheck =0,
        bigauntgutyear =0,
        bigauntpostGrandCheck =0,
        bigauntpostGrandyear =0,
        bigauntskinCheck=0,
        bigauntskinyear=0
        )
    else:
      p = person.bigAuntHistory(
        accountid = infos[0][0],
        optionhistorybigaunt = infos[0][1] ,  # not select
        bigauntbreastCheck= infos[0][2],
        bigauntbreastyear= infos[0][3],
        bigauntliverCheck =infos[0][4],
        bigauntliveryear =infos[0][5],
        bigauntgutCheck =infos[0][6],
        bigauntgutyear =infos[0][7],
        bigauntpostGrandCheck =infos[0][8],
        bigauntpostGrandyear =infos[0][9],
        bigauntskinCheck=infos[0][10],
        bigauntskinyear=infos[0][11]
        )
    return p
def insert_bigAuntHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.bigAuntHistory(
        accountid= int(user_id),
        optionhistorybigaunt = int(request.form.get('optionhistorybigaunt')) if not (request.form.get('optionhistorybigaunt'))=='' else 99,
        bigauntbreastCheck= int(request.form.get('bigauntbreastCheck')) if not (request.form.get('bigauntbreastCheck'))==None  else 0,
        bigauntbreastyear= int(request.form.get('bigauntbreastyear')) if not (request.form.get('bigauntbreastyear'))==None  else 0,
        bigauntliverCheck =int(request.form.get('bigauntliverCheck')) if not (request.form.get('bigauntliverCheck'))==None  else 0,
        bigauntliveryear =int(request.form.get('bigauntliveryear')) if not (request.form.get('bigauntliveryear'))=='' else 0,
        bigauntgutCheck = int(request.form.get('bigauntgutCheck')) if not (request.form.get('bigauntgutCheck'))==None  else 0,
        bigauntgutyear =int(request.form.get('bigauntgutyear')) if not (request.form.get('bigauntgutyear'))==''  else 0,
        bigauntpostGrandCheck = int(request.form.get('bigauntpostGrandCheck')) if not (request.form.get('bigauntpostGrandCheck'))==None  else 0,
        bigauntpostGrandyear =int(request.form.get('bigauntpostGrandyear')) if not (request.form.get('bigauntpostGrandyear'))=='' else 0,
        bigauntskinCheck= int(request.form.get('bigauntskinCheck')) if not (request.form.get('bigauntskinCheck'))==None  else 0,
        bigauntskinyear=int(request.form.get('bigauntskinyear')) if not (request.form.get('bigauntskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into bigaunt_history(bigaunthistoryid,optionhistorybigaunt,bigauntbreastcheck ,bigauntbreastyear ,bigauntlivercheck ,bigauntliveryear ,bigauntgutcheck ,'
       ' bigauntgutyear ,bigauntpostgrandcheck ,bigauntpostgrandyear ,bigauntskincheck  ,bigauntskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorybigaunt,p.bigauntbreastCheck,p.bigauntbreastyear,p.bigauntliverCheck,p.bigauntliveryear,p.bigauntgutCheck,
         p.bigauntgutyear,p.bigauntpostGrandCheck,p.bigauntpostGrandyear,p.bigauntskinCheck,p.bigauntskinyear
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติป้า  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติน้า
def get_smallAuntHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select smallaunthistoryid,optionhistorysmallaunt,smallauntbreastcheck ,smallauntbreastyear ,smallauntlivercheck ,smallauntliveryear ,smallauntgutcheck ,'
      ' smallauntgutyear ,smallauntpostgrandcheck ,smallauntpostgrandyear ,smallauntskincheck  ,smallauntskinyear ,created ,sh.id'
      ' from smallaunt_history sh join a_user u on sh.smallaunthistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.smallAuntHistory(
        accountid = 0,
        optionhistorysmallaunt = 99 ,  # not select
        smallauntbreastCheck= 0,
        smallauntbreastyear= 0,
        smallauntliverCheck =0,
        smallauntliveryear =0,
        smallauntgutCheck =0,
        smallauntgutyear =0,
        smallauntpostGrandCheck =0,
        smallauntpostGrandyear =0,
        smallauntskinCheck=0,
        smallauntskinyear=0
        )
    else:
      p = person.smallAuntHistory(
        accountid = infos[0][0],
        optionhistorysmallaunt = infos[0][1] ,  # not select
        smallauntbreastCheck= infos[0][2],
        smallauntbreastyear= infos[0][3],
        smallauntliverCheck =infos[0][4],
        smallauntliveryear =infos[0][5],
        smallauntgutCheck =infos[0][6],
        smallauntgutyear =infos[0][7],
        smallauntpostGrandCheck =infos[0][8],
        smallauntpostGrandyear =infos[0][9],
        smallauntskinCheck=infos[0][10],
        smallauntskinyear=infos[0][11]
        )
    return p
def insert_smallAuntHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.smallAuntHistory(
        accountid= int(user_id),
        optionhistorysmallaunt = int(request.form.get('optionhistorysmallaunt')) if not (request.form.get('optionhistorysmallaunt'))=='' else 99,
        smallauntbreastCheck= int(request.form.get('smallauntbreastCheck')) if not (request.form.get('smallauntbreastCheck'))==None  else 0,
        smallauntbreastyear= int(request.form.get('smallauntbreastyear')) if not (request.form.get('smallauntbreastyear'))==None  else 0,
        smallauntliverCheck =int(request.form.get('smallauntliverCheck')) if not (request.form.get('smallauntliverCheck'))==None  else 0,
        smallauntliveryear =int(request.form.get('smallauntliveryear')) if not (request.form.get('smallauntliveryear'))=='' else 0,
        smallauntgutCheck = int(request.form.get('smallauntgutCheck')) if not (request.form.get('smallauntgutCheck'))==None  else 0,
        smallauntgutyear =int(request.form.get('smallauntgutyear')) if not (request.form.get('smallauntgutyear'))==''  else 0,
        smallauntpostGrandCheck = int(request.form.get('smallauntpostGrandCheck')) if not (request.form.get('smallauntpostGrandCheck'))==None  else 0,
        smallauntpostGrandyear =int(request.form.get('smallauntpostGrandyear')) if not (request.form.get('smallauntpostGrandyear'))=='' else 0,
        smallauntskinCheck= int(request.form.get('smallauntskinCheck')) if not (request.form.get('smallauntskinCheck'))==None  else 0,
        smallauntskinyear=int(request.form.get('smallauntskinyear')) if not (request.form.get('smallauntskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into smallaunt_history(smallaunthistoryid,optionhistorysmallaunt,smallauntbreastcheck ,smallauntbreastyear ,smallauntlivercheck ,smallauntliveryear ,smallauntgutcheck ,'
       ' smallauntgutyear ,smallauntpostgrandcheck ,smallauntpostgrandyear ,smallauntskincheck  ,smallauntskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorysmallaunt,p.smallauntbreastCheck,p.smallauntbreastyear,p.smallauntliverCheck,p.smallauntliveryear,p.smallauntgutCheck,
         p.smallauntgutyear,p.smallauntpostGrandCheck,p.smallautpostGrandyear,p.smallauntskinCheck,p.smallauntskinyear
         
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติน้า  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติอา
def get_smallbroHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select smallbrohistoryid,optionhistorysmallbro,smallbrobreastcheck ,smallbrobreastyear ,smallbrolivercheck ,smallbroliveryear ,smallbrogutcheck ,'
      ' smallbrogutyear ,smallbropostgrandcheck ,smallbropostgrandyear ,smallbroskincheck  ,smallbroskinyear ,created ,sh.id'
      ' from smallbro_history sh join a_user u on sh.smallbrohistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.smallbroHistory(
        accountid = 0,
        optionhistorysmallbro = 99 ,  # not select
        smallbrobreastCheck= 0,
        smallbrobreastyear= 0,
        smallbroliverCheck =0,
        smallbroliveryear =0,
        smallbrogutCheck =0,
        smallbrogutyear =0,
        smallbropostGrandCheck =0,
        smallbropostGrandyear =0,
        smallbroskinCheck=0,
        smallbroskinyear=0
        )
    else:
      p = person.smallbroHistory(
        accountid = infos[0][0],
        optionhistorysmallbro = infos[0][1] ,  # not select
        smallbrobreastCheck= infos[0][2],
        smallbrobreastyear= infos[0][3],
        smallbroliverCheck =infos[0][4],
        smallbroliveryear =infos[0][5],
        smallbrogutCheck =infos[0][6],
        smallbrogutyear =infos[0][7],
        smallbropostGrandCheck =infos[0][8],
        smallbropostGrandyear =infos[0][9],
        smallbroskinCheck=infos[0][10],
        smallbroskinyear=infos[0][11]
        )
    return p
def insert_smallbroHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.smallbroHistory(
        accountid= int(user_id),
        optionhistorysmallbro = int(request.form.get('optionhistorysmallbro')) if not (request.form.get('optionhistorysmallbro'))=='' else 99,
        smallbrobreastCheck= int(request.form.get('smallbrobreastCheck')) if not (request.form.get('smallbrobreastCheck'))==None  else 0,
        smallbrobreastyear= int(request.form.get('smallbrobreastyear')) if not (request.form.get('smallbrobreastyear'))==None  else 0,
        smallbroliverCheck =int(request.form.get('smallbroliverCheck')) if not (request.form.get('smallbroliverCheck'))==None  else 0,
        smallbroliveryear =int(request.form.get('smallbroliveryear')) if not (request.form.get('smallbroliveryear'))=='' else 0,
        smallbrogutCheck = int(request.form.get('smallbrogutCheck')) if not (request.form.get('smallbrogutCheck'))==None  else 0,
        smallbrogutyear =int(request.form.get('smallbrogutyear')) if not (request.form.get('smallbrogutyear'))==''  else 0,
        smallbropostGrandCheck = int(request.form.get('smallbropostGrandCheck')) if not (request.form.get('smallbropostGrandCheck'))==None  else 0,
        smallbropostGrandyear =int(request.form.get('smallbropostGrandyear')) if not (request.form.get('smallbropostGrandyear'))=='' else 0,
        smallbroskinCheck= int(request.form.get('smallbroskinCheck')) if not (request.form.get('smallbroskinCheck'))==None  else 0,
        smallbroskinyear=int(request.form.get('smallbroskinyear')) if not (request.form.get('smallbroskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into smallbro_history(smallbrohistoryid,optionhistorysmallbro,smallbrobreastcheck ,smallbrobreastyear ,smallbrolivercheck ,smallbroliveryear ,smallbrogutcheck ,'
       ' smallbrogutyear ,smallbropostgrandcheck ,smallbropostgrandyear ,smallbroskincheck  ,smallbroskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorysmallbro,p.smallbrobreastCheck,p.smallbrobreastyear,p.smallbroliverCheck,p.smallbroliveryear,p.smallbrogutCheck,
         p.smallbrogutyear,p.smallbropostGrandCheck,p.smallbropostGrandyear,p.smallbroskinCheck,p.smallbroskinyear
         
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติอา  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติหลานชาย
def get_mengrandChildHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select mengrandchildhistoryid,optionhistorymengrandchild,mengrandchildbreastcheck ,mengrandchildbreastyear ,mengrandchildlivercheck ,mengrandchildliveryear ,mengrandchildgutcheck ,'
      ' mengrandchildgutyear ,mengrandchildpostgrandcheck ,mengrandchildpostgrandyear ,mengrandchildskincheck  ,mengrandchildskinyear ,created ,sh.id'
      ' from mengrandchild_history sh join a_user u on sh.mengrandchildhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.mengrandChildHistory(
        accountid = 0,
        optionhistorymengrandchild = 99 ,  # not select
        mengrandChildbreastCheck= 0,
        mengrandChildbreastyear= 0,
        mengrandChildliverCheck =0,
        mengrandChildliveryear =0,
        mengrandChildgutCheck =0,
        mengrandChildgutyear =0,
        mengrandChildpostGrandCheck =0,
        mengrandChildpostGrandyear =0,
        mengrandChildskinCheck=0,
        mengrandChildskinyear=0
        )
    else:
      p = person.mengrandChildHistory(
        accountid = infos[0][0],
        optionhistorymengrandchild = infos[0][1] ,  # not select
        mengrandChildbreastCheck= infos[0][2],
        mengrandChildbreastyear= infos[0][3],
        mengrandChildliverCheck =infos[0][4],
        mengrandChildliveryear =infos[0][5],
        mengrandChildgutCheck =infos[0][6],
        mengrandChildgutyear =infos[0][7],
        mengrandChildpostGrandCheck =infos[0][8],
        mengrandChildpostGrandyear =infos[0][9],
        mengrandChildskinCheck=infos[0][10],
        mengrandChildskinyear=infos[0][11]
        )
    return p
def insert_mengrandChildHistory(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.mengrandChildHistory(
        accountid= int(user_id),
        optionhistorymengrandchild = int(request.form.get('optionhistorymengrandchild')) if not (request.form.get('optionhistorymengrandchild'))=='' else 99,
        mengrandChildbreastCheck= int(request.form.get('mengrandChildbreastCheck')) if not (request.form.get('mengrandChildbreastCheck'))==None  else 0,
        mengrandChildbreastyear= int(request.form.get('mengrandChildbreastyear')) if not (request.form.get('mengrandChildbreastyear'))==None  else 0,
        mengrandChildliverCheck =int(request.form.get('mengrandChildliverCheck')) if not (request.form.get('mengrandChildliverCheck'))==None  else 0,
        mengrandChildliveryear =int(request.form.get('mengrandChildliveryear')) if not (request.form.get('mengrandChildliveryear'))=='' else 0,
        mengrandChildgutCheck = int(request.form.get('mengrandChildgutCheck')) if not (request.form.get('mengrandChildgutCheck'))==None  else 0,
        mengrandChildgutyear =int(request.form.get('mengrandChildgutyear')) if not (request.form.get('mengrandChildgutyear'))==''  else 0,
        mengrandChildpostGrandCheck = int(request.form.get('mengrandChildpostGrandCheck')) if not (request.form.get('mengrandChildpostGrandCheck'))==None  else 0,
        mengrandChildpostGrandyear =int(request.form.get('mengrandChildpostGrandyear')) if not (request.form.get('mengrandChildpostGrandyear'))=='' else 0,
        mengrandChildskinCheck= int(request.form.get('mengrandChildskinCheck')) if not (request.form.get('mengrandChildskinCheck'))==None  else 0,
        mengrandChildskinyear=int(request.form.get('mengrandChildskinyear')) if not (request.form.get('mengrandChildskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into mengrandChild_history(mengrandchildhistoryid,optionhistorymengrandChild,mengrandChildbreastcheck ,mengrandChildbreastyear ,mengrandChildlivercheck ,mengrandChildliveryear ,mengrandChildgutcheck ,'
       ' mengrandChildgutyear ,mengrandChildpostgrandcheck ,mengrandChildpostgrandyear ,mengrandChildskincheck  ,mengrandChildskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorymengrandchild,p.mengrandChildbreastCheck,p.mengrandChildbreastyear,p.mengrandChildliverCheck,p.mengrandChildliveryear,p.mengrandChildgutCheck,
         p.mengrandChildgutyear,p.mengrandChildpostGrandCheck,p.mengrandChildpostGrandyear,p.mengrandChildskinCheck,p.mengrandChildskinyear
         
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติหลานชาย  เรียบร้อย...' 
                flash(error)
                return p
#ประวัติหลานสาว
def get_womengrandChildHistoty(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select womengrandchildhistoryid,optionhistorywomengrandchild,womengrandchildbreastcheck ,womengrandchildbreastyear ,womengrandchildlivercheck ,womengrandchildliveryear ,womengrandchildgutcheck ,'
      ' womengrandchildgutyear ,womengrandchildpostgrandcheck ,womengrandchildpostgrandyear ,womengrandchildskincheck  ,womengrandchildskinyear ,created ,sh.id'
      ' from womengrandchild_history sh join a_user u on sh.womengrandchildhistoryid = u.id '
      ' where  u.id = %s order by sh.id DESC limit 1 ',(user_id,)
    )
    infos =cur.fetchall()
    if not infos:
      p = person.womengrandChildHistoty(
        accountid = 0,
        optionhistorywomengrandchild = 99 ,  # not select
        womengrandchildbreastCheck= 0,
        womengrandchildbreastyear= 0,
        womengrandchildliverCheck =0,
        womengrandchildliveryear =0,
        womengrandchildgutCheck =0,
        womengrandchildgutyear =0,
        womengrandchildpostGrandCheck =0,
        womengrandchildpostGrandyear =0,
        womengrandchildskinCheck=0,
        womengrandchildskinyear=0
        )
    else:
      p = person.womengrandChildHistoty(
        accountid = infos[0][0],
        optionhistorywomengrandchild = infos[0][1] ,  # not select
        womengrandchildbreastCheck= infos[0][2],
        womengrandchildbreastyear= infos[0][3],
        womengrandchildliverCheck =infos[0][4],
        womengrandchildliveryear =infos[0][5],
        womengrandchildgutCheck =infos[0][6],
        womengrandchildgutyear =infos[0][7],
        womengrandchildpostGrandCheck =infos[0][8],
        womengrandchildpostGrandyear =infos[0][9],
        womengrandchildskinCheck=infos[0][10],
        womengrandchildskinyear=infos[0][11]
        )
    return p
def insert_womengrandChildHistoty(user_id):
      error=None
      dbConn =get_db()
      cur =dbConn.cursor()
      p = person.womengrandChildHistoty(
        accountid= int(user_id),
        optionhistorywomengrandchild = int(request.form.get('optionhistorywomengrandchild')) if not (request.form.get('optionhistorywomengrandchild'))=='' else 99,
        womengrandchildbreastCheck= int(request.form.get('womengrandchildbreastCheck')) if not (request.form.get('womengrandchildbreastCheck'))==None  else 0,
        womengrandchildbreastyear= int(request.form.get('womengrandchildbreastyear')) if not (request.form.get('womengrandchildbreastyear'))==None  else 0,
        womengrandchildliverCheck =int(request.form.get('womengrandchildliverCheck')) if not (request.form.get('womengrandchildliverCheck'))==None  else 0,
        womengrandchildliveryear =int(request.form.get('womengrandchildliveryear')) if not (request.form.get('womengrandchildliveryear'))=='' else 0,
        womengrandchildgutCheck = int(request.form.get('womengrandchildgutCheck')) if not (request.form.get('womengrandchildgutCheck'))==None  else 0,
        womengrandchildgutyear =int(request.form.get('womengrandchildgutyear')) if not (request.form.get('womengrandchildgutyear'))==''  else 0,
        womengrandchildpostGrandCheck = int(request.form.get('womengrandchildpostGrandCheck')) if not (request.form.get('womengrandchildpostGrandCheck'))==None  else 0,
        womengrandchildpostGrandyear =int(request.form.get('womengrandchildpostGrandyear')) if not (request.form.get('womengrandchildpostGrandyear'))=='' else 0,
        womengrandchildskinCheck= int(request.form.get('womengrandchildskinCheck')) if not (request.form.get('womengrandchildskinCheck'))==None  else 0,
        womengrandchildskinyear=int(request.form.get('womengrandchildskinyear')) if not (request.form.get('womengrandchildskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into womengrandchild_history(womengrandchildhistoryid,optionhistorywomengrandchild,womengrandchildbreastcheck ,womengrandchildbreastyear ,womengrandchildlivercheck ,womengrandchildliveryear ,womengrandchildgutcheck ,'
       ' womengrandchildgutyear ,womengrandchildpostgrandcheck ,womengrandchildpostgrandyear ,womengrandchildskincheck  ,womengrandchildskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorywomengrandchild,p.womengrandchildbreastCheck,p.womengrandchildbreastyear,p.womengrandchildliverCheck,p.womengrandchildliveryear,p.womengrandchildgutCheck,
         p.womengrandchildgutyear,p.womengrandchildpostGrandCheck,p.womengrandchildpostGrandyear,p.womengrandchildskinCheck,p.womengrandchildskinyear
         
       )
    #   'insert into son_history(sonhistoryid) '
    #   ' values(%s) ',
    #  (p.accountid,)
      )
      if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติหลานสาว  เรียบร้อย...' 
                flash(error)
                return p
