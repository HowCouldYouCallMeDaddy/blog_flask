from . import auth
from .form import RegisterForm,Form
from flask import render_template, redirect, request, url_for, flash
from ..model import User
from .. import db

@auth.route('/register',methods=['GET','POST'])
def register():
    Form = RegisterForm()
    if(Form.validate_on_submit()):
        user = User(email=Form.email.data,username=Form.name.data,password=Form.password.data)
        db.session.add(user)
        flash("login now please")
    return render_template('auth/register.html', form=Form)


@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('auth/login.html')