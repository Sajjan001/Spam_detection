from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    message = TextAreaField('Enter message to check:', validators=[DataRequired()])
    submit = SubmitField('Check for Spam')