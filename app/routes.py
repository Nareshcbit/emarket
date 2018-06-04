from flask import render_template, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Naresh Madiraju'}
    parent_dict = [
        {'A':'val1','B':'val2'},
        {'C':'val3','D':'val4'}
        ]
    return render_template('index.html', title='Home', user=user, parent_dict = parent_dict)

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route('/nobootstrap')
def nobootstrap():
    return render_template('nobootstrap.html')

