from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import random
import sqlite3
import time
import os
from gtts import gTTS

#install flask, flask-sqlalchemy, GTTP

stringInput = 'Error'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)

connection = sqlite3.connect('inputString3.db')
cursor = connection.cursor()

def create_table():
    stringData = 'CREATE TABLE IF NOT EXISTS textData(datestamp TEXT, keyword TEXT, value TEXT)'
    cursor.execute(stringData)
def data_entry():
    insertData = 'INSERT INTO textData VALUES(1451255552, "2016-01-02", "Python","test")'
    cursor.execute(insertData)
    connection.commit()
    connection.close()
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = 'Hello World'
    cursor.execute("INSERT INTO textData(datestamp, keyword, value) VALUES (?, ?, ?)", 
                   (date, keyword, value))
    connection.commit()
def read_from_db():
    cursor.execute('SELECT * FROM textData')
    #data = cursor.fetchall()
    for data in cursor.fetchall():
        # Initialize gTTS with the text to convert
        speech = gTTS(data[2])

        # Save the audio file to a temporary file
        speech_file = 'speech.mp3'
        speech.save(speech_file)

        # Play the audio file
        os.system('start ' + speech_file)
# def __repr__(self):
#     return '<Task %r>' %self.id
create_table()
for i in range(1):
    dynamic_data_entry()
read_from_db()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return 'hello'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8001)