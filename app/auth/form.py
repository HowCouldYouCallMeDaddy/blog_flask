from wtforms import StringField,SubmitField,PasswordField,BooleanField
from flask_wtf import FlaskForm
from ..model import User
from wtforms import ValidationError
from wtforms.validators import DataRequired,Email,EqualTo


class LoginForm(FlaskForm):
    login_name = StringField("User Name or Email",[DataRequired()])
    password = PasswordField("Your password",[DataRequired()])
    submit = SubmitField("Submit")
    remember_me = BooleanField("remember me")

class RegisterForm(FlaskForm):
    email = StringField("Email",[DataRequired(),Email()])
    name = StringField("User Name",[DataRequired()])
    password = PasswordField("Your password",[DataRequired(),EqualTo('passwordConfirom')])
    passwordConfirom = PasswordField("Type your password again",[DataRequired()])
    submit = SubmitField("sunbmit")


    def validata_email(self):
        if User.query.filter_by(email=self.email.data).first() is not None:
            raise ValidationError('Email already registerd.')

    def validata_username(self):
        if User.query.filter_by(username=self.name.data).first() is not None:
            raise ValidationError('Username already registerd.')