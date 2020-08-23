from flask import(
    Blueprint,flash,g,redirect,render_template,session,request,url_for
)
from werkzeug.exceptions import abort
from chat.db import get_db
from chat.chatclass import person

bp =Blueprint('inform',__name__)


@bp.route('/',methods=('GET','POST'))
def index():
   
    error =None
    if not session.get('user_id') is None:
        user_id =session['user_id']
    else: return redirect(url_for('auth.login'))
    dbConn = get_db()
    # get information 
    cur =dbConn.cursor()
    cur.execute(
           'select accountid ,first_name,last_name,birthday,sex,idcard,phonenumber,email,nation,race,created'
            ' from person p join a_user u on p.accountid = u.id where u.id = %s order by u.id DESC LIMIT 1',(user_id,)
       )
    infos = cur.fetchall()  
    if not infos:
        p =  person.personinfo(
            accountid=0,
            fname = "",
            sname = "",
            birthday = "",
            sex = "0",
            idCard = "",
            phoneNumber = "",
            email = "",
            nation = "",
            race = ""
        )
       
    else:
        p =  person.personinfo(
                accountid = infos[0][0],
                fname = infos[0][1],
                sname = infos[0][2],
                birthday =infos[0][3],
                sex = infos[0][4],
                idCard= infos[0][5],
                phoneNumber =infos[0][6],
                email =infos[0][7],
                nation =infos[0][8],
                race = infos[0][9]
            )
    # get self history
    cur .execute(
        'select personhistoryid,optionhistorycacheck,beastcheck,bcayear,bothbreatcacheck,bovalcheck,bovalyear,bgutcheck,'
         'bgutyear,livercheck,bliveryear,postgrandcheck,bpostgrandyear,skincheck,bskinyear,created' 
         ' from  history_self h join a_user u on h.personhistoryid = %s order by u.id DESC LIMIT 1',(user_id,)
    )
    his =cur.fetchall()
    if not his:
        pHistory =person.personHistory(
            accountid = 0 ,
            historyCa = 0,
            breastCheck = 0,
            bCAyear = 0,
            bothbeastCheck = 0,
            bovalCheck = 0,
            bovalyear = 0,
            bgutCheck = 0,
            bgutyear = 0,
            liverCheck = 0,
            liveryear = 0,
            postGrandCheck = 0,
            postGrandyear = 0,
            skinCheck = 0,
            skinyear = 0
        )
    

    if request.method=='POST':
            p =  person.personinfo(
                    accountid = user_id,
                    fname = request.form.get('fname') ,
                    sname = request.form.get('sname'),
                    birthday = request.form.get('birthday'),
                    sex = int(request.form.get('sex')),
                    idCard = request.form.get('idCard'),
                    phoneNumber = request.form.get('phoneNumber'),
                    email = request.form.get('email'),
                    nation = request.form.get('nation'),
                    race = request.form.get('race')
                )   
           # insert person information
            cur.execute(
            "INSERT INTO person(accountid,first_name,last_name,birthday,sex,idcard,phonenumber,email,nation,race) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (p.accountid,p.fname,p.sname,p.birthday,p.sex,p.idCard,p.phoneNumber,p.email,p.nation,p.race)
            )  
            if error is None:
                 dbConn.commit()
                 error ='บันทึกข้อมมูลคุณ:' + p.fname + ' เรียบร้อย ...'  
            flash(error)
            #insert person history infomation   
            ph = person.personHistory(
                accountid=user_id,
                historyCa = request.form.get('optionhistoryCA'),
                breastCheck =request.form.get('breastCheck'),
                bCAyear = request.form.get('bCAyear'),
                bothbeastCheck = request.form.get('bothbeastCheck'),
                bovalCheck = request.form.get('bovalCheck'),
                bovalyear = request.form.get('bovalyear'),
                bgutCheck = request.form.get('bgutCheck'),
                bgutyear = request.form.get('bgutyear'),
                liverCheck =request.form.get('liverCheck'),
                liveryear = request.form.get('bliveryear'),
                postGrandCheck =request.form.get('postGrandCheck'),
                postGrandyear = request.form.get('bpostyear'),
                skinCheck = request.form.get('skinCheck'),
                skinyear = request.form.get('bskinyear')

            )
            cur.execute(
                "INSERT INTO history_self(personhistoryid,optionhistorycacheck,beastcheck,bcayear,bothbreatcacheck,bovalcheck,bovalyear,bgutcheck,"
                " bgutyear,livercheck,bliveryear,postgrandcheck,bpostgrandyear,skincheck,bskinyear) "
                " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                ()
            ) 
            if erro is None:
                dbConn.commit()
                error = 'บันทึกประวัติส่วนตัวคุณ: +'
            return render_template('inform/index.html',p=p)
    if error is not None:
        flash(error) 
    return render_template('inform/index.html',p=p)