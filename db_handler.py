import psycopg2
import constants
class DBHandler:
    def __init__(self):
        DBHandler.HOST = constants.HOST
        DBHandler.USER = constants.USER
        DBHandler.DBNAME = constants.DATABASE
        DBHandler.PASSWORD = constants.PASS
    HOST = constants.HOST
    USER = constants.USER
    DBNAME = constants.DATABASE
    PASSWORD = constants.PASS
    @staticmethod
    def get_mydb():
        if DBHandler.DBNAME == '':
            constants.init()
        db = DBHandler()
        mydb = db.connect()
        return mydb

    def connect(self):
        mydb = psycopg2.connect(
            host=DBHandler.HOST,
            user=DBHandler.USER,
            password=DBHandler.PASSWORD,
            database = DBHandler.DBNAME
            # charset = "utf8mb4"
        )
        return mydb