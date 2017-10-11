from wtforms import StringField,SubmitField
from flask_wtf import FlaskForm

class NameForm(FlaskForm):
    name = StringField("hi,type name")
    submit = SubmitField("Submit")