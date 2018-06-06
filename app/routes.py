from app import app, db

from flask import render_template, redirect, request
from app.forms import AddItemsForm, SearchItemsForm
from app.models import Items


app.secret_key = 'development key'

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
         return "Development in progress"
    else:
        return render_template('items_search.html', form=form)