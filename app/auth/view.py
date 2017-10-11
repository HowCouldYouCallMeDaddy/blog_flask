from . import auth
from .form import RegisterForm,Form
from flask import render_template, redirect, request, url_for, flash
from ..model import User

@auth.roeute('/register',methods=['GET','POST'])
def register():
    Form = RegisterForm()
    if(Form.validate_on_submit()):





@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('auth/login.html')