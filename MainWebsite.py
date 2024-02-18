from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3

#install flask, flask-sqlalchemy, GTTP

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)

connection = sqlite3.connect('inputString.db')
cursor = connection.cursor()



def __repr__(self):
    return '<Task %r>' %self.id

dataString = """CREATE TABLE IF NOT EXISTS stringdata(string data)"""
cursor.execute(dataString)
results = cursor.fetchall()
print(results)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return 'hello'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8001)