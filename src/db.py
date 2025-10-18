from dotenv import dotenv_values
import mysql.connector

env = dotenv_values('.env') 

conn = None
cur = None

def connect():
    global conn
    global cur
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user=env['SQL_USER'],
        password=env['SQL_PSWD'],
    )
    cur = conn.cursor()

def close():
    global conn
    if conn != None:
        conn.close()


