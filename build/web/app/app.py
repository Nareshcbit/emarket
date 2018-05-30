# flask_web/app.py

from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_mysqldb import MySQL
import yaml



app = Flask(__name__)

# Configure db
db = yaml.load(open('dbconf.yaml'))
app.config['MYSQL_HOST'] = db['DB_HOST']
app.config['MYSQL_USER'] = db['DB_USER']
app.config['MYSQL_PASSWORD'] = db['DB_USER_PASSWORD']
app.config['MYSQL_DB'] = db['DB_NAME']


mysql = MySQL(app)

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