from flask import(
    Blueprint,flash,g,redirect,render_template,session,request,url_for
)
from werkzeug.exceptions import abort
from  chat.db import get_db
from chat.chatclass import person
#import history_related
from chat import history_related
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
    fh = history_related.get_fatherHistory(user_id)
    #ประวัติการตรวจในแม่
    mh = history_related.get_motherrHistory(user_id)
    #ประวัติการตรวจในพี่/น้อง(ชาย)
    broh = history_related.get_brotherHistory(user_id)
    #ประวัติการตรวจในพี่/น้อง(หญิง)
    sish = history_related.get_sisterHistory(user_id)
    #ประวัติการตรวจในทวด(ชาย)
    mgfh =history_related.get_mangrandfaHistory(user_id)
    #ประวัติการตรวจในทวด(หญิง)
    mgmh = history_related.get_womangrandMomHistory(user_id)
    #ประวัติการตรวจในปู่
    gfh = history_related.get_grandFatherHistory(user_id)
    #ประวัติการตรวจในย่า
    gmh =history_related.get_grandMomHistory(user_id)
    #ประวัติการตรวจในตา
    fomh =history_related.get_fatherOfMomHistory(user_id)
    #ประวัติการตรวจในยาย
    momh =history_related.get_motherOfMomHistory(user_id)
    #ประวัติการตรวจในลุง
    bunh = history_related.get_bigUncleHistory(user_id)
    #ประวัติการตรวจในป้า
    bauh =history_related.get_bigAuntHistory(user_id)
    #ประวัติการตรวจในน้า
    sauh =history_related.get_smallAuntHistory(user_id)
    #ประวัติการตรวจในอา
    smbh =history_related.get_smallbroHistory(user_id)
    #ประวัติการตรวจในหลาน(ชาย)
    mgch =history_related.get_mengrandChildHistory(user_id)
    #ประวัติการตรวจในหลาน(หญิง)
    wgch =history_related.get_womengrandChildHistoty(user_id)
    #ประวัติการตรวจในเหลน(ชาย)
    thgch =history_related.get_thirdmengrandChildHistory(user_id)
    #ประวัติการตรวจในเหลน(หญิง)
    twgch =history_related.get_thirdwomendgrandChildHistoty(user_id)
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
            #บันทึกประวัติพ่่อ
            fh = history_related.insert_fatherHistory(user_id)
            #บันทึกประวัติแม่
            mh =history_related.insert_motherHistory(user_id) 
            # บันทีกประวัิตน้องชาย
            broh =history_related.insert_brotherHistory(user_id)
            #บันทึกประวัติน้องสาว
            sish = history_related.insert_sisterHistory(user_id)
            #บันทึกประวัติทวดชาย
            mgfh = history_related.insert_mangrandfaHistory(user_id)
            #บันทุกประวัติทวดหญิง
            mgmh = history_related.insert_womangrandMomHistory(user_id)
            #บันทึกประวัติปู่
            gfh = history_related.insert_grandFatherHistory(user_id)   
            #บันทึกประวัติย่า
            gmh = history_related.insert_grandMomHistory(user_id)
            #ประวัติตา
            fomh = history_related.insert_fatherOfMomHistory(user_id)
            #ประวัติยาย
            momh =history_related.insert_motherOfMomHistory(user_id)
            #ประวัติลุง
            bunh =history_related.insert_bigUncleHistory(user_id)
            #ประวัติป้า
            bauh =history_related.insert_bigAuntHistory(user_id)
            #ประวัติน้า
            sauh = history_related.insert_smallAuntHistory(user_id)
            #ประวัติอา
            smbh = history_related.insert_smallbroHistory(user_id)
            #ประวัติหลานชาย
            mgch = history_related.insert_mengrandChildHistory(user_id)
            #ประวัติหลานสาว
            wgch = history_related.insert_womengrandChildHistoty(user_id)
            #ประวัติเหลนชาย
            thgch =history_related.insert_thirdmengrandChildHistory(user_id)
            #ประวัติเหลนสาว
            twgch =history_related.insert_thirdwomendgrandChildHistoty(user_id)

            return render_template('inform/index.html',p=p,ph=ph,sonh=sonh,dah=dah,fh=fh,mh=mh,
                                   broh=broh,sish=sish,mgfh=mgfh,mgmh=mgmh,gfh=gfh,gmh=gmh,fomh=fomh,momh=momh,
                                  bunh=bunh,bauh=bauh,sauh=sauh,smbh=smbh,mgch=mgch,wgch=wgch,thgch=thgch,twgch=twgch)
    if error is not None:
        flash(error) 
    return render_template('inform/index.html',p=p,ph=ph,sonh=sonh,dah=dah,fh=fh,mh=mh,
                     broh=broh,sish=sish,mgfh=mgfh,mgmh=mgmh,gfh=gfh,gmh=gmh,fomh=fomh,momh=momh,
                     bunh=bunh,bauh=bauh,sauh=sauh,smbh=smbh,mgch=mgch,wgch=wgch,thgch=thgch,twgch=twgch)