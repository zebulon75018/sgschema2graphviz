from flask import Flask, request, render_template, url_for

import json
import os
import subprocess

app = Flask(__name__)
#
# Route.
#
@app.route('/getschema',methods=["GET", "POST"])
def getschema():

    sd = request.form.get("subdomain","")
    sn = request.form.get("scriptname","")
    sk = request.form.get("scriptkey","")
    subprocess.run(["python",
                "getshemaSG.py",
                "--nameserver",
                sd,
                "--scriptname",
                sn,
                "--scriptkey",
                sk,
                ])
    return ""

# faire generation de class python ...
@app.route('/')
def home():
    if os.path.exists('schema.json') is False:
        return render_template('shotgun.html')

    with open('schema.json') as f:
        data = json.load(f)
    return render_template('index.html', entities=data)

if __name__ == '__main__':
    app.run(debug=True,port=5050)
