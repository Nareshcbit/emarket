from app import app, db

from flask import render_template, redirect, request
from flask import jsonify
from app.forms import AddItemsForm, SearchItemsForm
from app.models import Items, ItemsSchema
from redis import Redis
import redis
import hashlib
import json


app.secret_key = 'development key'
R_SERVER = redis.Redis('192.168.0.18', port=6379)
items_schema = ItemsSchema(many=True)

@app.route('/')
@app.route('/index')
@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
  
    form = SearchItemsForm()
    found_in_cache = 'False'
    if request.method == 'POST':
        search_category = request.form['Category']
        matched_items = Items.query.filter_by(Category=search_category).all()
        return render_template('homepage.html', form=form, MyItems = matched_items, found_in_cache = found_in_cache)  
    else:

        items_all = Items.query.all()
        return render_template('homepage.html', form=form, MyItems = items_all, found_in_cache = found_in_cache)


@app.route('/items_add', methods=['GET', 'POST'])
def items_add():
  
    form = AddItemsForm()
    if request.method == 'POST':
        newitem = Items(request.form['Category'], request.form['Vendor'], request.form['Model'], request.form['Price'])
        db.session.add(newitem)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('items_add.html', form=form)

@app.route('/redis', methods=['GET', 'POST'])
def redis():
  
    form = SearchItemsForm()
    found_in_cache = 'False'
    if request.method == 'POST':
        search_category = request.form['Category']
        matched_items = Items.query.filter_by(Category=search_category).all()
        result = items_schema.dump(matched_items)
        return jsonify(result.data)
    else:

        items_all = Items.query.all()
        return render_template('redis.html', form=form, MyItems = items_all, found_in_cache = found_in_cache)
