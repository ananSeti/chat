import functools
import psycopg2
from flask import(
    Blueprint ,flash,g,redirect,render_template,request,session,url_for
)

from werkzeug.security import check_password_hash,generate_password_hash
from chat.db import get_db

bp =Blueprint('auth',__name__,url_prefix='/auth')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view

@bp.before_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        dbConn = get_db()
        cur = dbConn.cursor()
        cur.execute("SELECT * FROM a_user WHERE id = %s", (user_id,))
        g.user = cur.fetchone()

@bp.route('/register',methods=('GET','POST'))
def register():
    if request.method=='POST':
        username =request.form['username']
        password =request.form['password']

        dbConn = get_db()

        #dbConn = psycopg2.connect(host="127.0.0.1",port=5432,database="chatbot", user = "anan",password="anan1234")
        cur =dbConn.cursor()

        error =None
        
        if not username:
            error ='ป้อนชื่อ...'
        elif not password:
            error ='ป้อนรหัสผ่าน password'
        else:
            cur.execute("SELECT id FROM a_user WHERE username = %s", (username,))
            row =cur.fetchone()
             
            if row is not None:  
                 error = 'User {} ลงทะเบียนไปแล้ว'.format(username)
                 error = error +" id is :" + str(row[0])
                 #error = 'Usersss {} is already registered'.format(row)
                                   

            #error =f'User {username} is already registered.'
        if error is None:
                           
            cur.execute(   
            "INSERT INTO a_user (username, password) VALUES (%s, %s)",
                (username, generate_password_hash(password))
            )
           
            dbConn.commit()
            return redirect(url_for('auth.login'))

        flash(error)
    return render_template('auth/register.html')


@bp.route('/login',methods=('GET','POST'))
def login():
        if request.method =='POST':
            username = request.form['username']
            password = request.form['password']
            dbConn =get_db()
            cur =dbConn.cursor()
            error =None
            cur.execute('SELECT * FROM a_user WHERE username = %s', (username,))
            user =cur.fetchone()
            
            if user is None:
                error ='username ไม่ถูกต้อง' 
                                         #user['password']       
            elif not check_password_hash(user[2],password):
                error ='password ไม่ถูกต้อง'
            #else:
            #   error =  str(user[2])
            if error is None:
                session.clear()
                session['user_id'] = user[0]  #userID
                return redirect(url_for('inform.index')) #chang index to inform
            flash(error)
        return render_template('auth/login.html')
@bp.route('/info',methods=('GET','POST'))
def info():
    if request.method =='POST':
       username =request.form['username']
       password =request.form['password']
       db =get_db()
       error =None
       if not username:
          error ='Username is require.'
       elif not password:
          error ='Password is required.'
       elif(
          db.excecute("SELECT id FROM a_user WHERE username = %s", (username,)).fethone()
          is not None
        ):
        error = f'User {username} is already required.'
       if error is None:
          db.execute(
            "INSERT INTO a_user (username, password) VALUES (?, ?)",
             (username, generate_password_hash(password)),
          ) 
          db.commit()
          return render_template(url_for('auth/login'))
       flash(error)

    return render_template('auth/info.html')

@bp.route('/test',methods=('GET','POST'))
def test():
    return "test"
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
