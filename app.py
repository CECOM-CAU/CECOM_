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

if __name__ == '__main__':
    IP = str(socket.gethostbyname(socket.gethostname()))
    app.run(host="192.168.0.20", port=9090, debug=True)