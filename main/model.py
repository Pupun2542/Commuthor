from main import db, login_manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import pymysql
from main import bcrypt


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


class user(db.Model, UserMixin):
    UserID = db.Column(db.Integer(), primary_key=True)
    UserName = db.Column(db.String(length=255), nullable=False, unique=True)
    Password_hash = db.Column(db.String(length=255), nullable=False)
    Email = db.Column(db.String(length=255), nullable=False, unique=True)
    SMLink = db.Column(db.String(length=255))
    Style = db.Column(db.String(length=12))
    Privacy = db.Column(db.String(length=12))

    def get_id(self):
        return self.UserID

    def __repr__(self):
        return f'user {self.UserName}'

    @property
    def Password(self):
        return self.Password

    @Password.setter
    def Password(self, plaintextpassword):
        self.Password_hash = bcrypt.generate_password_hash(plaintextpassword).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.Password_hash, attempted_password)
