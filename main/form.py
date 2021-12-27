from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from main import backend
from main.model import user


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        ss = user.query.filter_by(UserName=username_to_check.data).first()
        if ss:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = user.query.filter_by(Email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='Username', validators=[Length(min=2, max=32)])
    email = StringField(label='Email', validators=[Email()])
    password1 = PasswordField(label='Password', validators=[Length(min=6)])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1')])
    submit = SubmitField(label='Sign up')


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[Email()])
    password = PasswordField(label='Password', validators=[Length(min=6)])
    submit = SubmitField(label='Sign in')
    rememberme = BooleanField(label='Remember Me')


