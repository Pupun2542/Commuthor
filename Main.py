from flask import Flask, render_template, redirect, session, url_for, request
from  flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.secret_key = "123123123"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "commuthor"

db = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'email' in request.form and 'password' in request.form:
            email = request.form['email']
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("select * from user where Email=%s and Password=%s", (email, password))
            records = cursor.fetchone()
            if records is not None:
                # if records['Email'] == email and records['Password'] == password:
                session['loginsuccess'] = True
                return redirect(url_for('home'))
            else:
                return redirect(url_for('index'))
    return render_template("login.html")


@app.route("/home")
def home():
    if session['loginsuccess']:
        return render_template("home.html")
    else:
        return redirect(url_for('index'))


@app.route("/logout")
def logout():
    session['loginsuccess'] = False
    return redirect(url_for('index'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        if "username" in request.form and "email" in request.form and "password" in request.form:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            if request.form['password'] == request.form['c_password']:
                cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute("insert into commuthor.user(UserName, Email, Password) values(%s,%s,%s)",
                               (username, email, password))
                db.connection.commit()
                return redirect(url_for('index'))

            else:
                return "password mismatch"

    return render_template("register.html")



if __name__ == '__main__':
    app.run(debug=True)
