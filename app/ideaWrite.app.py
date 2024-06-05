#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Wangs_official@MewCako
import json
import os
import time

import requests
from flask import Flask, render_template, redirect
from werkzeug.serving import run_simple

versioncode = json.loads(open("../version.json").read())["version"]
api_url = 'http://localhost:65371/'

app = Flask(__name__, template_folder='static/templates')


@app.route('/')
def index_page(LTime=time.strftime("%Y/%m/%d %H:%M",
                                   time.localtime(json.loads(requests.get(f'{api_url}/start').text)['LastLogin'])),
               NovelInfo='0'):
    if not os.path.exists("install.lock"):
        return redirect('/setup')
    else:
        ni_res = requests.get(f'{api_url}/get/novel')
        if ni_res.status_code == 200:
            NovelInfo = json.loads(ni_res.text)
        elif ni_res.status_code == 500:
            return render_template('error.html', pth='/get/novel/', Error_info=ni_res.text, VersionCode=versioncode,
                                   statuscode=ni_res.status_code)
        idea_res = requests.get(f'{api_url}/get/idea')
        if idea_res.status_code == 200:
            ideainfo = json.loads(idea_res.text)
        elif idea_res.status_code == 500:
            return render_template('error.html', pth='/get/idea/', Error_info=idea_res.text, VersionCode=versioncode,
                                   statuscode=idea_res.status_code)
        db_res = requests.get(f'{api_url}/get/dashboard')
        if db_res.status_code == 200:
            db = json.loads(db_res.text)
        elif db_res.status_code == 500:
            return render_template('error.html', pth='/get/dashboard/', Error_info=db_res.text, VersionCode=versioncode,
                                   statuscode=db_res.status_code)
        return render_template('main.html', versionCode=versioncode, lastlogin=LTime, NovelInfo=NovelInfo,
                               IdeaInfo=ideainfo, db=db)


@app.route('/setup')
def setup():
    if not os.path.exists("install.lock"):
        return render_template('setup.html')
    else:
        return redirect('/')


if __name__ == "__main__":
    run_simple('localhost', 65370, app)
