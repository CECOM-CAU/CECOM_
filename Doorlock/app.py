from flask import Flask, request
import json
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
        return userAuthendication(thejson[1:])
    if returnjson[0] == 'w:':
        return userRegister(thejson[1:])
    if returnjson[0] == 'e':
        return userDelete(thejson[1:])