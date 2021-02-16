from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# create a Class from FlaskForm and add custom parameters for the project
class inputData(FlaskForm):
    item = StringField('Task')
    command = StringField('Command')
    example = StringField('Example')
    submit = SubmitField('Submit Item')