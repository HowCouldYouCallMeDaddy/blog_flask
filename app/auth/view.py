from . import auth
from flask import render_template, redirect, request, url_for, flash


@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('auth/login.html')