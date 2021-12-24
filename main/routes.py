from main import db, app
from flask import render_template, redirect, session, url_for, request, flash, get_flashed_messages
import MySQLdb
from main import backend as services
from main.form import RegisterForm, LoginForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm
    # if request.method == 'POST':
    #     if 'email' in request.form and 'password' in request.form:
    #         email = request.form['email']
    #         password = request.form['password']
    #         cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    #         cursor.execute("select * from user where Email=%s and Password=%s", (email, password))
    #         records = cursor.fetchone()
    #         if records is not None:
    #             # if records['Email'] == email and records['Password'] == password:
    #             session['loginsuccess'] = True
    #             return redirect(url_for('home'))
    #         else:
    #             return redirect(url_for('index'))
    return render_template("login.html", form=form)


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
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = services.encryptpassword(form.password1.data)

        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("insert into commuthor.user(UserName, Email, Password) values(%s,%s,%s)",
                       (username, email, password))
        db.connection.commit()
        return redirect(url_for('index'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template("register.html", form=form)
