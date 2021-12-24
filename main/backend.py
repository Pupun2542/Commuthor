from main import db
import MySQLdb


def checkdupemail(email):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from user where Email=%s", email)
    records = cursor.fetchone()
    if records is None:
        return True
    return False


def checkdupeUser(user):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from user where Username=%s", user)
    records = cursor.fetchone()
    if records is None:
        return True
    return False
