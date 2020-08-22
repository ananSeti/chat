import psycopg2
from flask import current_app,g
def get_db():
    #try:
        if 'dbConn' not in g:
         g.dbConn = psycopg2.connect(host="127.0.0.1",port=5432,database="chatbot", user = "anan",password="anan1234")
         
        return g.dbConn
    #except:
    #    return 
def close_db(e=None):
    dbConn = g.pop('dbConn',None)

    if dbConn is not None:
        dbConn.close()


