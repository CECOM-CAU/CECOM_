from flask import Flask, url_for, render_template, request, redirect, session
import json
import cecom_doorlock
import User_Authentication
import socket

app = Flask(__name__)
app.secret_key = 'We are Fried Chicken Dinner!!!!'

@app.route("/doorLock", methods=['GET', 'POST'])
def doorLock():
    if request.method == 'POST':
        getJson = request.get_json(silent=True, cache=False, force=True)
        if getJson:
            returnjson = json.dumps(getJson)
        else:
            returnjson = "no json"
        print(returnjson)
        if returnjson[0] == 'q':
            return User_Authentication.Authentication(returnjson[1:])
        if returnjson[0] == 'w:':
            return cecom_doorlock.userRegister(returnjson[1:])
        if returnjson[0] == 'e':
            return cecom_doorlock.userDelete(returnjson[1:])
    if request.method == 'GET':
        return 'test'
@app.route("/", methods=['GET', 'POST'])
def main():
    return "hello world"

if __name__ == '__main__':
    IP = str(socket.gethostbyname(socket.gethostname()))
    app.run(host=IP, port=5010, debug=True)