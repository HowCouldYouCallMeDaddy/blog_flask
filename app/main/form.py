from wtforms import StringField,SubmitField,PasswordField,ValidationError
from flask_wtf import FlaskForm
from ..model import User

class Form(FlaskForm):
    name = StringField("hi,type name")
    password = PasswordField("Your password")
    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    email = StringField("Email")
    name = StringField("User Name")
    password = PasswordField("Your password")
    passwordConfirom = PasswordField("Type your password again")

    def validata_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registerd.')

    def validata_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registerd.')