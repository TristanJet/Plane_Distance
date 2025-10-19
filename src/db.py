from dotenv import dotenv_values
import mysql.connector

env = dotenv_values('.env') 

conn = None
cur = None

class UninitiatedError(Exception):
    def __init__(self, message="SQL not initiated"):
        self.message = message
        super().__init__(self.message)

def connect():
    global conn
    global cur
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user=env['SQL_USER'],
        password=env['SQL_PSWD'],
        database="flight_game",
    )
    cur = conn.cursor()

def close():
    global conn
    if conn == None: raise UninitiatedError
    conn.close()

def distinctCountryRange(min, max):
    global cur
    if cur == None: raise UninitiatedError
    query = ("SELECT DISTINCT iso_country FROM airport "
             "WHERE longitude_deg BETWEEN %s AND %s")
    cur.execute(query, (min, max))
    return list(map(lambda x: x[0], cur.fetchall()))

def test():
    global cur
    connect()
    countries = distinctCountryRange(-180, -170)
    print(countries)
    close()

test()

# def getLongRange(min, max):
#     global cur
#     if cur == None: return
#     query = ""
#     cur.execute(query, (min, max))
#
