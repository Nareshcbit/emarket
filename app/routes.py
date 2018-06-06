from app import app, db

from flask import render_template, redirect, request
from app.forms import ContactForm, UserForm, AddItemsForm
from app.models import User, Items


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
        user = User(request.form['username'], request.form['email'])
        db.session.add(user)
        db.session.commit()
        return redirect('/user_list')
    else:
        return render_template('user_add.html', form=form)

@app.route('/user_list')
def user_list():
  
    users = User.query.all()
    return render_template('user_list.html', users = users)



@app.route('/items_list')
def items_list():
    itemsList_temp = [
        {'Uid':'1','Vendor':'Dell', 'Category':'Laptop', 'Model':'XPS' ,'Price':800},
        {'Uid':'2','Vendor':'Apple', 'Category':'Laptop', 'Model':'Macbook Air' ,'Price':1000},
        {'Uid':'3','Vendor':'Apple', 'Category':'Mobile', 'Model':'iPhoneX' ,'Price':1200},
        {'Uid':'5','Vendor':'Samsung', 'Category':'Mobile', 'Model':'S9' ,'Price':1100},
        ]

    items_all = Items.query.all()
    return render_template('items_list.html', MyItems = items_all)  

@app.route('/items_add', methods=['GET', 'POST'])
def items_add():
  
    form = AddItemsForm()
    if request.method == 'POST':
        newitem = Items(request.form['Vendor'], request.form['Category'], request.form['Model'], request.form['Price'])
        db.session.add(newitem)
        db.session.commit()
        return redirect('/items_list')
    else:
        return render_template('items_add.html', form=form)