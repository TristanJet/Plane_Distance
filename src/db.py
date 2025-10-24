from dotenv import dotenv_values
import mysql.connector

env = dotenv_values('.env') 

'''
ONLY through wrapper functions should these values be accessed
NEVER directly write
'''
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
        database=env['DATABASE'],
    )
    cur = conn.cursor()

def close():
    global conn
    if conn == None: raise UninitiatedError
    conn.close()

def getCountriesInRange(min, max):
    global cur
    if cur == None: raise UninitiatedError
    query = ("SELECT DISTINCT iso_country FROM airport "
             "WHERE longitude_deg BETWEEN %s AND %s")
    cur.execute(query, (min, max))
    return list(map(lambda x: x[0], cur.fetchall()))

''' Only municipality is NULLable, rest of values are guaranteed '''
def getAirports(c, min, max):
    global cur
    if cur == None: raise UninitiatedError 
    query = ("SELECT ap.name, c.name as country, ap.municipality, ap.latitude_deg, ap.longitude_deg "
             "FROM airport as ap INNER JOIN country as c "
             "WHERE ap.iso_country = %s AND "
             "ap.iso_country = c.iso_country AND "
             "ap.longitude_deg BETWEEN %s AND %s "
             "ORDER BY ap.longitude_deg")
    cur.execute(query, (c, min, max))
    return cur.fetchall()

def test():
    import random
    global cur
    min = 0
    max = 20
    connect()
    countries = getCountriesInRange(min, max)
    airports = getAirports(random.choice(countries), min, max)
    print(random.choice(airports))
    close()

# test()
