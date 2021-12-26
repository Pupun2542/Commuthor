from main import db, login_manager
from main import bcrypt
import MySQLdb
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from user where UserID=%s", [user_id])
    records = cursor.fetchone()
    return records

def getUserId(email):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select UserID from user where Email=%s", [email])
    records = cursor.fetchone()
    return records[0][0]


def checkdupemail(email):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from user where Email=%s", [email])
    records = cursor.fetchone()
    if records is None:
        return True
    return False


def checkdupeuser(user):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from user where Username=%s", [user])
    records = cursor.fetchone()
    if records is None:
        return True
    return False


def encryptpassword(plaintextpassword):
    return bcrypt.generate_password_hash(plaintextpassword).decode('utf-8')


def checkemail(email):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from user where Email=%s", [email])
    records = cursor.fetchone()
    if records is not None:
        return True
    return False


def checkpassword(email, pw):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from user where email=%s,password=%s", [email, pw])
    records = cursor.fetchone()
    if records is not None:
        return True
    return False


def getuserfrommail(email):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from user where email=%s", [email])
    return cursor.fetchone[0][0]
