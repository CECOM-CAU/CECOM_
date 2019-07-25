from flask import Flask, request
import json
import User_Authentication
import cecom_doorlock
app = Flask(__name__)

@app.route("/doorLock", methods=['GET', 'POST'])
def doorLock():
    getJson = request.get_json(silent=True, cache=False, force=True)
    if getJson:
        returnjson = json.dumps(getJson)
    else:
        returnjson = "no json"
    print(returnjson)
    if returnjson[0] == 'q':
        return Authentication(returnjson[1:])
    if returnjson[0] == 'w:':
        return userRegister(returnjson[1:])
    if returnjson[0] == 'e':
        return userDelete(returnjson[1:])