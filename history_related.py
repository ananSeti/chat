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
      ' mothergutyear ,motherpostgrandcheck ,motherpostgrandyear ,motherskincheck  ,motherskinyear ,created '
      ' from mother_history sh join a_user u on sh.motherhistoryid = u.id '
      ' where  u.id = %s order by motherhistoryid DESC limit 1 ',(user_id,)
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
        motherbreastCheck= int(request.form.get('motherbreatCheck')) if not (request.form.get('motherbreatCheck'))==None  else 0,
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
# def get_brotherrHistory(user_id):
#     error =None
#     dbConn = get_db()
#     cur =dbConn.cursor()
#     #select
#     cur.execute(
#       'select brotherhistoryid,optionhistorybrother,brotherbreastcheck ,brotherbreastyear ,brotherlivercheck ,brotherliveryear ,brothergutcheck ,'
#       ' brothergutyear ,brotherpostgrandcheck ,brotherpostgrandyear ,brotherskincheck  ,brotherskinyear ,created '
#       ' from brother_history sh join a_user u on sh.brotherhistoryid = u.id '
#       ' where  u.id = %s order by brotherhistoryid DESC limit 1 ',(user_id,)
#     )
#     infos =cur.fetchall()
#     if not infos:
#       p = person.brotherHistory(
#         accountid = 0,
#         optionhistorybrother = 99 ,  # not select
#         brotherbreastCheck= 0,
#         brotherbreastyear= 0,
#         brotherliverCheck =0,
#         brotherliveryear =0,
#         brothergutCheck =0,
#         brothergutyear =0,
#         brotherpostGrandCheck =0,
#         brotherpostGrandyear =0,
#         brotherskinCheck=0,
#         brotherskinyear=0
#         )
#     else:
#       p = person.brotherHistory(
#         accountid = infos[0][0],
#         optionhistorybrother = infos[0][1] ,  # not select
#         brotherbreastCheck= infos[0][2],
#         brotherbreastyear= infos[0][3],
#         brotherliverCheck =infos[0][4],
#         brotherliveryear =infos[0][5],
#         brothergutCheck =infos[0][6],
#         brothergutyear =infos[0][7],
#         brotherpostGrandCheck =infos[0][8],
#         brotherpostGrandyear =infos[0][9],
#         brotherskinCheck=infos[0][10],
#         brotherskinyear=infos[0][11]
#         )
#     return p
#ประวัติน้องชาย
def get_brotherHistory(user_id):
    error =None
    dbConn = get_db()
    cur =dbConn.cursor()
    #select
    cur.execute(
      'select brotherhistoryid,optionhistorybrother,brotherbreastcheck ,brotherbreastyear ,brotherlivercheck ,brotherliveryear ,brothergutcheck ,'
      ' brothergutyear ,brotherpostgrandcheck ,brotherpostgrandyear ,brotherskincheck  ,brotherskinyear ,created '
      ' from brother_history sh join a_user u on sh.brotherhistoryid = u.id '
      ' where  u.id = %s order by brotherhistoryid DESC limit 1 ',(user_id,)
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
        optionhistorybrother = int(request.form.get('optionhistorybrother')) if not (request.form.get('optionhistorybrother'))==None else 99,
        brotherbreastCheck= int(request.form.get('brotherbreatCheck')) if not (request.form.get('brotherbreatCheck'))==None  else 0,
        brotherbreastyear= int(request.form.get('brotherbreastyear')) if not (request.form.get('brotherbreastyear'))==None  else 0,
        brotherliverCheck =int(request.form.get('brotherliverCheck')) if not (request.form.get('brotherliverCheck'))==None  else 0,
        brotherliveryear =int(request.form.get('brotherliveryear')) if not (request.form.get('brotherliveryear'))=='' else 0,
        brothergutCheck = int(request.form.get('brothergutCheck')) if not (request.form.get('brothergutCheck'))==None  else 0,
        brothergutyear =int(request.form.get('brothergutyear')) if not (request.form.get('brothergutyear'))==''  else 0,
        brotherpostGrandCheck = int(request.form.get('brotherpostGrandCheck')) if not (request.form.get('brotherpostGrandCheck'))==None  else 0,
        brotherpostGrandyear =int(request.form.get('brotherpostGrandyear')) if not (request.form.get('brotherpostGrandyear'))=='' else 0,
        brotherskinCheck= int(request.form.get('brotherskinCheck')) if not (request.form.get('brotherskinCheck'))==None  else 0,
        brotherskinyear=int(request.form.get('brotherskinyear')) if not (request.form.get('brorskinyear'))==''  else 0,
      )
      cur.execute(
       'insert into brother_history(brotherhistoryid,optionhistorybrother,brotherbreastcheck ,brotherbreastyear ,brotherlivercheck ,brotherliveryear ,brothergutcheck ,'
       ' brothergutyear ,brotherpostgrandcheck ,brotherpostgrandyear ,brotherskincheck  ,brotherskinyear )'
       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ',
       ( p.accountid,p.optionhistorybrother,p.brotherbreastCheck,p.brotherbreastyear,p.brotherlivercheck,p.brotherliveryear,p.brothergutCheck,
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
      ' sistergutyear ,sisterpostgrandcheck ,sisterpostgrandyear ,sisterskincheck  ,sisterskinyear ,created '
      ' from sister_history sh join a_user u on sh.sisterhistoryid = u.id '
      ' where  u.id = %s order by sisterhistoryid DESC limit 1 ',(user_id,)
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
        optionhistorysister = int(request.form.get('optionhistorysister')) if not (request.form.get('optionhistorysister'))==None else 99,
        sisterbreastCheck= int(request.form.get('sisterbreatCheck')) if not (request.form.get('sisterbreatCheck'))==None  else 0,
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
