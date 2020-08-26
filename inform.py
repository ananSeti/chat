from flask import(
    Blueprint,flash,g,redirect,render_template,session,request,url_for
)
from werkzeug.exceptions import abort
from chat.db import get_db
from chat.chatclass import person
import history_related

bp =Blueprint('inform',__name__)


@bp.route('/',methods=('GET','POST'))
def index():
   
    error =None
    if not session.get('user_id') is None:
        user_id =session['user_id']
    else: return redirect(url_for('auth.login'))
    dbConn = get_db()
    # ข้อมูลสาวนตัว get information 
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
    # ประวัติส่วนตัว get self history
    cur .execute(
        'select personhistoryid,optionhistorycacheck,beastcheck,bcayear,bothbreatcacheck,bovalcheck,bovalyear,bgutcheck,'
         'bgutyear,livercheck,bliveryear,postgrandcheck,bpostgrandyear,skincheck,bskinyear,created' 
         ' from  history_self h join a_user u on h.personhistoryid = %s order by h.id DESC LIMIT 1',(user_id,)
    )
    his =cur.fetchall()
    if not his:
        ph =person.personHistory(
            accountid = 0 ,
            historyCa = 99,
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
    else:
        ph = person.personHistory(
            accountid=his[0][0],
            historyCa=his[0][1],
            breastCheck=his[0][2],
            bCAyear=his[0][3],
            bothbeastCheck=his[0][4],
            bovalCheck=his[0][5],
            bovalyear=his[0][6],
            bgutCheck=his[0][7],
            bgutyear=his[0][8],
            liverCheck=his[0][9],
            liveryear=his[0][10],
            postGrandCheck=his[0][11],
            postGrandyear=his[0][12],
            skinCheck=his[0][13],
            skinyear=his[0][14]
        )
    # ประวัติการตรวจมะเร็งในบุตรชาย
    sonh=history_related.get_sonHistory(user_id)
    #ประวัตรการตรวจในบุตรสาว
    dah = history_related.get_daugtherHistory(user_id)        
    #ประวัติการตรวจในพ่อ
    #ประวัติการตรวจในแม่
    #ประวัติการตรวจในพี่/น้อง(ชาย)
    #ประวัติการตรวจในพี่/น้อง(หญิง)
    #ประวัติการตรวจในทวด(ชาย)
    #ประวัติการตรวจในทวก(หญิง)
    #ประวัติการตวจในปู่
    #ประวัติการตรวจในย่า
    #ประวัติการตรวจในตา
    #ประวัติการตรวจในยาย
    #ประวัติการตีรวจในลุง
    #ประวัติการตรวจในป้า
    #ประวัติการตาวจในน้า
    #ประวัติการตรวจในอา
    #ประวัติการตรวจในหลาน(ชาย)
    #ประวัติกสนตรวจในหลาน(หญิง)
    #ประวัติการตรวจในเหลน(ชาย)
    #ประวัติการตรวจในเหลน(หญิง)
    
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
            error=None
            ph = person.personHistory(
                accountid=user_id,
                historyCa = int(request.form.get('optionhistoryCA')) if not (request.form.get('optionhistoryCA'))==None  else 0,
                breastCheck =int(request.form.get('breastCheck')) if not (request.form.get('breastCheck'))==None  else 0,
                bCAyear = int(request.form.get('bCAyear')) if not (request.form.get('bCAyear'))==''  else 0,
                bothbeastCheck = int(request.form.get('bothbeastCheck')) if not (request.form.get('bothbeastCheck'))==None  else 0 ,
                bovalCheck = request.form.get('bovalCheck') if not (request.form.get('bovalCheck'))==None  else 0,
                bovalyear = int(request.form.get('bovalyear')) if not (request.form.get('bovalyear'))==''  else 0,
                bgutCheck = request.form.get('bgutCheck')if not (request.form.get('bgutCheck'))==None  else 0,
                bgutyear = int(request.form.get('bgutyear')) if not (request.form.get('bgutyear'))==''  else 0,
                liverCheck =request.form.get('liverCheck') if not (request.form.get('liverCheck'))==None  else 0,
                liveryear = int(request.form.get('bliveryear')) if not (request.form.get('bliveryear'))==''  else 0,
                postGrandCheck =request.form.get('postGrandCheck') if not (request.form.get('postGrandCheck'))==None  else 0,
                postGrandyear = int(request.form.get('bpostyear')) if not (request.form.get('bpostyear'))==''  else 0,
                skinCheck = request.form.get('skinCheck') if not (request.form.get('skinCheck'))==None  else 0,
                skinyear =   int(request.form.get('bskinyear')) if not (request.form.get('bskinyear'))==''  else 0
                  
            )
            cur.execute(
                "INSERT INTO history_self(personhistoryid,optionhistorycacheck,beastcheck,bcayear,bothbreatcacheck,bovalcheck,bovalyear,bgutcheck,"
                " bgutyear,livercheck,bliveryear,postgrandcheck,bpostgrandyear,skincheck,bskinyear) "
                " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (ph.accountid,ph.historyCa,ph.breastCheck,ph.bCAyear,ph.bothbeastCheck,ph.bovalCheck,ph.bovalyear,ph.bgutCheck,
                ph.bgutyear,ph.liverCheck,ph.liveryear,ph.postGrandCheck,ph.postGrandyear,ph.skinCheck,ph.skinyear
                )
            ) 
            if error is None:
                dbConn.commit()
                error = 'บันทึกประวัติส่วนตัวคุณ: ' + p.fname + ' เรียบร้อย...' 
                flash(error)
            # บันทึกประวัติลูกชาย
            sonh = history_related.insert_sonHistory(user_id)
            #บันทีกประวัติลูกสาว
            dah = history_related.insert_daugterHistory(user_id)
            return render_template('inform/index.html',p=p,ph=ph,sonh=sonh,dah=dah)
    if error is not None:
        flash(error) 
    return render_template('inform/index.html',p=p,ph=ph,sonh=sonh,dah=dah)