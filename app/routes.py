from flask import render_template, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Naresh Madiraju'}
    return render_template('index.html', title='Home', user=user)

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route('/nobootstrap')
def nobootstrap():
    return render_template('nobootstrap.html')

