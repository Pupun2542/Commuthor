from main import db, app, login_manager
from flask import render_template, redirect, session, url_for, request, flash, get_flashed_messages
import MySQLdb
from main import backend as services
from main.model import user
from main.form import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/', methods=['GET', 'POST'])
def main():
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = user.query.filter_by(Email=form.email.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.UserID}', category='success')
            return redirect(url_for('home'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route("/home")
# @login_required
def home():
    return render_template("home.html")


@app.route("/logout")
def logout():
    logout_user()
    flash("logged out", category='info')
    return redirect(url_for('index'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = user(UserName=form.username.data,
                              Email=form.email.data,
                              Password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('index'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template("register.html", form=form)
