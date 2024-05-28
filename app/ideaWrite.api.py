from flask import Flask, render_template, request, send_from_directory , jsonify , session , redirect , url_for
import os
from werkzeug.serving import run_simple
import sqlite3
import time
from flask_cors import CORS
import yaml
import json
import shutil

app = Flask(__name__)
CORS(app)

@app.route('/')
def index_api():
    return jsonify({'status':'OK'})
    
@app.route('/setup')
def setup():
    return render_template('setup.html')

@app.route('/start')
def start():
    time_now = int(time.time())
    conn = sqlite3.connect('./data/main.db')
    c = conn.cursor()
    cursor = c.execute("select * from MAIN limit 1;")
    for row in cursor:
        LastLogin = row[2]
    c.execute(f"UPDATE MAIN set LastLogin = {time_now} where ID=1")
    conn.commit()
    return {'LastLogin':LastLogin}

@app.route('/get/novel')
def get_novel():
    try:
        returninfo = []
        conn = sqlite3.connect('./data/main.db')
        c = conn.cursor()
        cursor = c.execute('SELECT * FROM MAIN')
        for cur in cursor:
            print(cur)
            try:
                if len(cur[3]) == 0:
                    # No Novel
                    return {'novel': None}, 404
            except TypeError:
                    return {'novel': None}, 404
            else:
                conn = sqlite3.connect('./data/main.db')
                c = conn.cursor()
                cursor = c.execute("select * from MAIN limit 1;")
                for row in cursor:
                    NovelID = row[3].split(',')
                for nid in NovelID:
                    with open(f'data/novel/{nid}/info.yml', 'r', encoding='utf-8') as f:
                        y = yaml.safe_load(f)
                        ctime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(y['CreateTime']))
                        ac = len(os.listdir(f'data/novel/{nid}/chapter/'))
                        alltext_o = 0
                        file_list = os.listdir(f'data/novel/{nid}/chapter/')
                        for file_name in file_list:
                            if file_name.endswith('.txt'):
                                file_path = os.path.join(f'data/novel/{nid}/chapter/', file_name)
                                with open(file_path, 'r', encoding='utf-8') as file:
                                    content = file.read()
                                    word_count = len(content)
                                    alltext_o += word_count
                        returninfo.append({'id':nid,'title':y['title'],'about':y['about'],'CreateTime':ctime,'allChapter':ac,'allText':alltext_o})
                return returninfo
                
    except Exception as e:
         return jsonify({'PythonErrorInfo':str(e)}),500

@app.route('/create/novel', methods=['GET'])
def create_novel():
    try:
        FirstUse = ''
        novelid = request.args.get('id')
        novelid_b =  ',' + request.args.get('id')
        title = request.args.get('title')
        about = request.args.get('about')

        conn = sqlite3.connect('./data/main.db')
        c = conn.cursor()
        cursor = c.execute("select * from MAIN limit 1;")
        for row in cursor:
            novelid_o = row[3]
            if len(novelid_o) == 0:
                FirstUse = True
        novelid_b = str(novelid_o) + str(novelid_b)
        if FirstUse:
            c.execute(f"UPDATE MAIN set NovelID = '{novelid}' where ID=1")
        elif not FirstUse:
            c.execute(f"UPDATE MAIN set NovelID = '{novelid_b}' where ID=1")
        conn.commit()
        
        os.makedirs(f'data/novel/{novelid}')
        os.makedirs(f'data/novel/{novelid}/chapter')
        os.makedirs(f'data/novel/{novelid}/settings')
        data = {'id':novelid,'title':title,'about':about,'CreateTime':int(time.time())}
        with open(f'data/novel/{novelid}/info.yml', 'w', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)
        f.close
        return {'status':'ok'}
    except Exception as e:
         return jsonify({'PythonErrorInfo':str(e)}),500
    
@app.route('/del/novel')
def del_novel():
    try:
        conn = sqlite3.connect('./data/main.db')
        c = conn.cursor()
        cursor = c.execute("select * from MAIN limit 1;")
        for row in cursor:
            NovelID = row[3]
        willdel = request.args.get('id')
        data_list = [x.strip() for x in NovelID.split(",")]
        if willdel in data_list:
            data_list.remove(willdel)
            data = ",".join(data_list)
        else:
            return jsonify({'APIErrorInfo':'此ID不存在'}),500
        # del sql
        c.execute(f"UPDATE MAIN set NovelID = '{data}' where ID=1")
        conn.commit()
        # del file
        shutil.rmtree(f'data/novel/{willdel}')
        return jsonify({'status':'ok'})
    except Exception as e:
        return jsonify({'PythonErrorInfo':str(e)}),500

if __name__ == "__main__":
    run_simple('localhost', 65371, app)