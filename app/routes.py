from flask import render_template, redirect, request
from app.forms import ContactForm, UserForm

from app import app

app.secret_key = 'development key'

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Naresh Madiraju'}
    parent_dict = [
        {'Uid':'1','Vendor':'Dell', 'Category':'Laptop', 'Model':'XPS' ,'Price':800},
        {'Uid':'2','Vendor':'Apple', 'Category':'Laptop', 'Model':'Macbook Air' ,'Price':1000},
        {'Uid':'3','Vendor':'Apple', 'Category':'Mobile', 'Model':'iPhoneX' ,'Price':1200},
        {'Uid':'4','Vendor':'Samsung', 'Category':'Mobile', 'Model':'S9' ,'Price':1100},
        ]
    return render_template('index.html', title='Home', user=user, parent_dict = parent_dict)

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route('/nobootstrap')
def nobootstrap():
    return render_template('nobootstrap.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
 
    if request.method == 'POST':
        return 'Form posted.'
 
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@app.route('/user_add', methods=['GET', 'POST'])
def user_add():
  
    form = UserForm()
    if request.method == 'POST':
        return redirect('Development in Progress')
    else:
        return render_template('user_add.html', form=form)