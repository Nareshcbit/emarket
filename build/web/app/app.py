# flask_web/app.py

from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_mysqldb import MySQL
from redis import Redis
import yaml
import redis 
import hashlib



app = Flask(__name__)

# Configure db
yaml_config = yaml.load(open('config.yaml'))
app.config['MYSQL_HOST'] = yaml_config['DB_HOST']
app.config['MYSQL_USER'] = yaml_config['DB_USER']
app.config['MYSQL_PASSWORD'] = yaml_config['DB_USER_PASSWORD']
app.config['MYSQL_DB'] = yaml_config['DB_NAME']
mysql = MySQL(app)

#Configure Redis
REDIS_SERVER = redis.Redis(yaml_config['REDIS_HOST'], port=6379)


@app.route("/")
@app.route("/index")
@app.route("/items")
def items_list():
  cursor = mysql.connection.cursor()
  cursor.execute("SELECT * from items")
  items = cursor.fetchall()

  #return str(data)
  cursor.close()
  return render_template('items_list.html', items = items)

@app.route("/items_search", methods=['GET', 'POST'])
def items_search():
  if request.method == 'POST':
    searchDetails = request.form
    search_field = searchDetails['search_field']
    return search_field
  else:
    return render_template('items_search.html')


@app.route('/items_add', methods=['GET', 'POST'])
def items_add():
  
  if request.method == 'POST':
    itemDetails = request.form
    vendor = itemDetails['vendor']
    category = itemDetails['category']
    model = itemDetails['model']
    cost = itemDetails['cost']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO items (vendor,category,model,cost) VALUES (%s,%s,%s,%s)", (vendor,category,model,cost))  
    cursor = mysql.connection.cursor()
    mysql.connection.commit()
    cursor.close()

    return redirect('/items_list')
  else:
    return render_template('items_add.html')



if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0',port=5000)