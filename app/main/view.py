from . import main
from .form import NameForm
from flask import render_template,session

@main.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name']=form.name.data
        return render_template('index.html',form=form,name=session.get('name'),know=session.get('know'))
    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           know=session.get('know'))