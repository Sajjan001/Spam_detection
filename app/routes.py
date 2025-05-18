from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import MessageForm
from app.models.spam_classifier import SpamClassifier

main_bp = Blueprint('main', __name__)
spam_classifier = SpamClassifier()

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = MessageForm()
    result = None
    
    if form.validate_on_submit():
        message = form.message.data
        result = spam_classifier.predict(message)
        
    return render_template('index.html', form=form, result=result)