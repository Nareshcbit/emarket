# flask_web/app.py

from flask import Flask, render_template, request
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
	data = cursor.fetchall()
	return data
    #return render_template('authors.html')
@app.route('/authors_add', methods=['GET', 'POST'])
def authors_add():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        authorDetails = request.form
        id = authorDetails['id']
        firstname = authorDetails['firstname']
        lastname = authorDetails['lastname']
        return id
    else:

        return render_template('authors_add.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)