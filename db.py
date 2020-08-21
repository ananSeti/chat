import psycopg2

def get_db():
    #try:
        dbConn = psycopg2.connect(host="127.0.0.1",port=5432,database="chatbot", user = "anan",password="anan1234")
         
        return dbConn
    #except:
    #    return 
    

