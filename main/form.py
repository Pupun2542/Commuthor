from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email = StringField(label='email')
    password1 = PasswordField(label='password')
    password2 = PasswordField(label='confirm password')
    submit = SubmitField(label='Sign up')
