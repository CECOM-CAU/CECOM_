import sqlite3

from flask import Flask, url_for, render_template, request, redirect, session
import json
import cecom_doorlock
import User_Authentication
import socket

app = Flask(__name__)
app.secret_key = 'We are Fried Chicken Dinner!!!!'

@app.route("/", methods=['GET', 'POST'])
def doorLock():
    if request.method == 'POST':
        returnjson = request.get_json(silent=True, cache=False, force=True)
        if returnjson['code'] == '1':
            print(returnjson['ID'])
            return User_Authentication.Authentication(returnjson['ID'])
        return str(returnjson)
    if request.method == 'GET':
        return 'test'
@app.route("/communication", methods=['GET', 'POST'])
def main():
    return "hello world"

@app.route("/signIn", methods=['GET', 'POST'])
def registerPage():
    if request.method == 'GET':
        return render_template('sign_in.html')
    else:
        id = request.form['id']
        name = request.form['name']
        conn = sqlite3.connect("test.db")
        curs = conn.cursor()
        curs.execute("select*from User")
        curs.execute("INSERT INTO user(Student_ID,Name) VALUES(" + "'"+ str(id)+"'" + "," + "'" + str(name)+ "'" + ")")
        conn.commit()
        curs.close()
        conn.close()
    return "test"

@app.route("/log", methods=['GET', 'POST'])
def logPage():
    conn = sqlite3.connect('fileLogDB.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM fileLogDB")
    sqlData = curs.fetchall()
    returnString = ""
    for i in sqlData:
        returnString +=( "<h1>"+str(i)+"</h1>")
    conn.commit()
    curs.close()
    conn.close()
    return returnString


def DBinit():
    conn = sqlite3.connect("test.db")
    curs = conn.cursor()
    curs.execute("DROP TABLE IF EXISTS User")
    curs.execute("CREATE TABLE if not exists User(Student_ID, Name);")
    conn.commit()
    curs.close()
    conn.close()

    conn = sqlite3.connect("fileLogDB.db")
    curs = conn.cursor()
    curs.execute("CREATE TABLE  if not exists fileLogDB(username, time, file)")
    conn.commit()
    curs.close()
    conn.close()

    conn = sqlite3.connect("test.db")
    curs = conn.cursor()
    curs.execute("select*from User")
    curs.execute("INSERT INTO user(Student_ID,Name) VALUES("    +  '20178999'  + "," + "'testdata'" + ")")
    conn.commit()
    curs.close()
    conn.close()

if __name__ == '__main__':
    DBinit()
    IP = str(socket.gethostbyname(socket.gethostname()))
    app.run(host="192.168.0.20", port=9090, debug=True)