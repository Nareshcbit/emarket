# flask_web/app.py

from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_mysqldb import MySQL
import yaml



app = Flask(__name__)

# Configure db
db = yaml.load(open('dbconf.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']


mysql = MySQL(app)

@app.route("/")
@app.route("/index")
@app.route("/items")
def list_items():
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * from items")
	items = cursor.fetchall()

	#return str(data)
	cursor.close()
	return render_template('items.html', items = items)




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)