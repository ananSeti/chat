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
      'select sonHistoryId,optionhistoryson,sonbreastcheck,sonbreastyear,sonliverCheck,sonliveryear,songutCheck,'
      ' songutyear,sonpostGrandCheck,sonpostGrandYear,sonskinCheck,sonskinyear,created '
      ' from son_history sh join a_user u on sh.sonHistoryId = u.id '
      ' where  u.id = %s order by u.id DESC limit 1 ',(user_id,)
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