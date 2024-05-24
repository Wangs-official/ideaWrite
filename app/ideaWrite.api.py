from flask import Flask, render_template, request, send_from_directory , jsonify , session , redirect , url_for
import os
import sqlite3
from werkzeug.serving import run_simple

app = Flask(__name__)

@app.route('/')
def index_api():
    return jsonify({'status':'OK'})
    
@app.route('/setup')
def setup():
    return render_template('setup.html')

if __name__ == "__main__":
    app.run('localhost', 65371, app , use_reloader=False)