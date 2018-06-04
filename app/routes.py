from flask import render_template, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Naresh Madiraju'}
    parent_dict = [
        {'uid':'1','vendor':'Dell', 'category':'Laptop', 'model':'XPS' ,'price':800},
        {'uid':'2','vendor':'Apple', 'category':'Laptop', 'model':'Macbook Air' ,'price':1000},
        {'uid':'3','vendor':'Apple', 'category':'Mobile', 'model':'iPhoneX' ,'price':1200},
        {'uid':'4','vendor':'Samsung', 'category':'Mobile', 'model':'S9' ,'price':1100},
        ]
    return render_template('index.html', title='Home', user=user, parent_dict = parent_dict)

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route('/nobootstrap')
def nobootstrap():
    return render_template('nobootstrap.html')

