from flask import Flask
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = "9691e12715cf4959ccb52384028c2b0c"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "commuthor"

db = MySQL(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from main import routes

