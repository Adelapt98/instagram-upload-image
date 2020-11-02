import datetime
import constants
from db_handler import *

def insertOrUpdate(script):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute(script)
    mydb.commit()

def select(script):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute(script)
    results = cursor.fetchall()
    return results