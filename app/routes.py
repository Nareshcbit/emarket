from flask import render_template, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Naresh Madiraju'}
    return render_template('index.html', title='Home', user=user)

