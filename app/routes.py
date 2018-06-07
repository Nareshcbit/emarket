from app import app, db

from flask import render_template, redirect, request
from app.forms import AddItemsForm, SearchItemsForm
from app.models import Items



app.secret_key = 'development key'
R_SERVER = redis.Redis('192.168.0.18', port=6379)

@app.route('/')
@app.route('/index')
@app.route('/items_list')
def items_list():

    items_all = Items.query.all()
    return render_template('items_list.html', MyItems = items_all)  

@app.route('/items_add', methods=['GET', 'POST'])
def items_add():
  
    form = AddItemsForm()
    if request.method == 'POST':
        newitem = Items(request.form['Category'], request.form['Vendor'], request.form['Model'], request.form['Price'])
        db.session.add(newitem)
        db.session.commit()
        return redirect('/items_list')
    else:
        return render_template('items_add.html', form=form)

@app.route('/items_search', methods=['GET', 'POST'])
def items_search():
  
    form = SearchItemsForm()
    if request.method == 'POST':

        search_category = request.form['Category']
        key = search_category

        matched_items = Items.query.filter_by(Category=search_category).all()
        return render_template('items_list.html', MyItems = matched_items)  
    else:
        return render_template('items_search.html', form=form)


@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
  
    form = SearchItemsForm()
    if request.method == 'POST':

        search_category = request.form['Category']
        key = search_category

        matched_items = Items.query.filter_by(Category=search_category).all()
        return render_template('homepage.html', form=form, MyItems = matched_items)  
    else:

        items_all = Items.query.all()
        return render_template('homepage.html', form=form, MyItems = items_all)
