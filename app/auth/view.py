from . import auth
from .form import RegisterForm,LoginForm
from flask import render_template, redirect, request, url_for, flash,session
from ..model import User
from .. import db
from flask_login import login_user,logout_user,login_required,current_user
from sqlalchemy import or_
from wtforms import ValidationError
from ..email import send_email


@auth.route('/register',methods=['GET','POST'])
def register():
    Form = RegisterForm()
    if(Form.validate_on_submit()):
        try:
            Form.validata_email()
            Form.validata_username()
            user = User(email=Form.email.data,username=Form.name.data,password=Form.password.data)
            db.session.add(user)
            db.session.commit()
            token = user.generate_confirmation_token()
            send_email(user.email,'Confirm your Email', 'auth/email/confirm', user=user, token=token)
            flash("Congratulation! We have sent you an Email, Please Confirm!")
            flash("login now please")
            return redirect(url_for('auth.login'))
        except ValidationError as e:
            flash(e.message)
    return render_template('auth/register.html', form=Form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash("Thanks for your confirm!")
    else:
        flash("How do you get the token?")
    return redirect(url_for('main.index'))


@auth.route('/login',methods=['GET','POST'])
def login():
    Form = LoginForm()
    if Form.validate_on_submit():
        print str(User.query.filter(User.username==Form.login_name.data or User.email==Form.login_name.data))
        user = User.query.filter(or_(User.username==Form.login_name.data,User.email==Form.login_name.data)).first()
        #user = User.query.filter_by(username=LoginForm.name.data).first()
        if user is not None and user.verify_password(Form.password.data):
            login_user(user,Form.remember_me.data)
            return redirect(url_for('main.index'))
        else:
            flash("check your email/username or password")
    return render_template('auth/login.html',form=Form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
