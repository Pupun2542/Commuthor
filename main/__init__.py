from flask import Flask
# from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

app.secret_key = "9691e12715cf4959ccb52384028c2b0c"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/commuthor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config["MYSQL_HOST"] = "localhost"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = ""
# app.config["MYSQL_DB"] = "commuthor"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "index"
login_manager.login_message_category = "info"
from main import routes

