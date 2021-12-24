from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from main import backend


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        if not backend.checkdupeUser(username_to_check):
            raise ValidationError('Username Already Exist!')

    def validate_email(self, email_to_check):
        if not backend.checkdupemail(email_to_check):
            raise ValidationError('email Already Exist!')

    username = StringField(label='Username', validators=[Length(min=2, max=32)])
    email = StringField(label='Email', validators=[Email()])
    password1 = PasswordField(label='Password', validators=[Length(min=6)])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1')])
    submit = SubmitField(label='Sign up')


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[Email()])
    password = PasswordField(label='Password', validators=[Length(min=6)])
    submit = SubmitField(label='Sign in')
