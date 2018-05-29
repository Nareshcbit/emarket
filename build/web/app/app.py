# flask_web/app.py

from flask import Flask, render_template, request, redirect
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
def index():
    return render_template('index.html')

@app.route("/authors")
def authors():
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * from authors_tbl")
	authors = cursor.fetchall()

	#return str(data)
	cursor.close()
	return render_template('authors.html', authors = authors)

@app.route('/authors_add', methods=['GET', 'POST'])
def authors_add():
    
    if request.method == 'POST':

        authorDetails = request.form
        firstname = authorDetails['firstname']
        lastname = authorDetails['lastname']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO authors_tbl (author_firstname,author_lastname) VALUES (%s,%s)", (firstname,lastname))  
        cursor = mysql.connection.cursor()
        mysql.connection.commit()
        cursor.close()

        return redirect('/authors')
    else:
        return render_template('authors_add.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)