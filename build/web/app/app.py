# flask_web/app.py

from flask import Flask, render_template
import yaml


app = Flask(__name__)

# Configure db
db = yaml.load(open('dbconf.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']


 
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/authors")
	return render_template('authors.html')
 
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)