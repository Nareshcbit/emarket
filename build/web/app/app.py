# flask_web/app.py

from flask import Flask
from flask import Response
from flask import request
#from redis import Redis
from datetime import datetime
import MySQLdb
import sys
#import redis 
import time
import hashlib
import os
import json


app = Flask(__name__)

dbconnection = MySQLdb.connect(host="192.168.0.13",
                        user = "naresh",
                        passwd = "P@ssword",
                        db = "mydb")
cursor = dbconnection.cursor()


 
@app.route("/")
def hello():
    return "Hello World!"

@app.route('/authors')
def get_authors():
        cursor.execute("select * from mydb.authors_tbl")
        return data
 
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)