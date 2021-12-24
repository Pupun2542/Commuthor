from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "123123123"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "commuthor"

db = MySQL(app)

from main import routes
