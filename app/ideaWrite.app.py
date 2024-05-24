from flask import Flask, render_template, request, send_from_directory , jsonify , session , redirect , url_for
from werkzeug.serving import run_simple
import os
import sqlite3
import json

versioncode = json.loads(open("../version.json").read())["version"]

app = Flask(__name__,template_folder='static/templates')
@app.route('/')
def index_page():
    # if not os.path.exists("install.lock"):
    #     return redirect('/setup')
    # else:
    #     return render_template('main.html')
    return render_template('main.html', versionCode=versioncode)

@app.route('/setup')
def setup():
    if not os.path.exists("install.lock"):
        return render_template('setup.html')
    else:
        return redirect('/')

if __name__ == "__main__":
    run_simple('0.0.0.0', 65370, app)