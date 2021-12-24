from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "9691e12715cf4959ccb52384028c2b0c"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "commuthor"

db = MySQL(app)

from main import routes

