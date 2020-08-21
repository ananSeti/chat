import functools
import psycopg2
from flask import(
    Blueprint ,flash,g,redirect,render_template,request,session,url_for
)

from werkzeug.security import check_password_hash,generate_password_hash
from chat.db import get_db

bp =Blueprint('auth',__name__,url_prefix='/auth')

@bp.route('/register',methods=('GET','POST'))
def register():
    if request.method=='POST':
        username =request.form['username']
        password =request.form['password']

        dbConn = get_db()

        #dbConn = psycopg2.connect(host="127.0.0.1",port=5432,database="chatbot", user = "anan",password="anan1234")
        cur =dbConn.cursor()

        error =None
        rows = None
        #print(error)

        cur.execute("SELECT id FROM a_user WHERE username = %s", (username,))
        rows =cur.fetchall() 
        for row in rows:
            #print(row[0]) 
            error ='User {} is already registered'.format(username)
        if not username:
            error ='Username is required.'
        elif not password:
            error ='Password is required.'
        elif(
             #db.execute("SELECT id FROM a_user WHERE username = %s", (username,)
             cur.execute("SELECT id FROM a_user WHERE username = %s", (username,))
             #cur.fetchone()  #is not None:
             #row =cur.fetchone()
             #rows = cur.fetchall() 
              #  for row in rows:  
              #  error = 'User {} is already registered'.format(username)
            ):
            error = 'Usersss {} is already registered'.format(username)
                                   

            #error =f'User {username} is already registered.'
        if error is None:
            #the name is available, store in the database and go to
            #the login page
            #cur = db.cursor()
            #db.execute(
            print(username)   
            cur.execute(   
            "INSERT INTO a_user (username, password) VALUES (%s, %s)",
                (username, generate_password_hash(password))
            )
            #db.commit()
            dbConn.commit()
            return redirect(url_for('auth.login'))

        flash(error)
    return render_template('auth/register.html')

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

@bp.route('/login',methods=('GET','POST'))
def login():
        if request.method =='POST':
            username = request.form['username']
            password = request.form['password']
            db =get_db()
            error =None
            user = db.execute('SELECT * FROM a_user WHERE username = %s', (username,)
            )
            #user =users.fetchone()
            
            if user is None:
                error ='Incorrect username'
            elif not check_password_hash(user['password'],password):
                error ='Incorrenct password'
            
            if error is None:
                session.clear()
                session['user_id'] = user['id']
                return redirect(url_for('index'))
            flash(error)
        return render_template('auth/login.html')
@bp.route('/test',methods=('GET','POST'))
def test():
    return "test"
