#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Wangs_official@MewCako
import os
import random
import shutil
import sqlite3
import time

import yaml
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from werkzeug.serving import run_simple

app = Flask(__name__)
CORS(app)


@app.route('/')
def index_api():
    return jsonify({'status': 'OK'})


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
    return {'LastLogin': LastLogin}


@app.route('/get/dashboard')
def get_dashboard(alltext_o=0):
    try:
        conn = sqlite3.connect('./data/main.db')
        c = conn.cursor()
        cursor = c.execute("select * from MAIN limit 1;")
        for row in cursor:
            jt = row[1]
            lt = row[2]
            xs = row[3].split(',')
            xs_o = row[3]
        Use_Time_Day = int((lt - jt) / 86400)
        All_Book = 0
        if len(str(xs_o)) > 4:
            All_Book = len(xs)
        if not All_Book == 0:
            for nid in xs:
                file_list = os.listdir(f'data/novel/{nid}/chapter/')
                for file_name in file_list:
                    if file_name.endswith('.txt'):
                        file_path = os.path.join(f'data/novel/{nid}/chapter/', file_name)
                        with open(file_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                            word_count = len(content)
                            alltext_o += word_count
        conn = sqlite3.connect('./data/idea.db')
        c = conn.cursor()
        cursor = c.execute('SELECT * FROM IDEA')
        All_idea = 0
        for row in cursor:
            All_idea = All_idea + 1
        return {'Use_Time_Day': Use_Time_Day, 'All_Book': All_Book, 'All_Text': alltext_o, 'All_Think': All_idea}
    except Exception as e:
        print(f"出现异常:{e}")
        return jsonify({'PythonErrorInfo': str(e)}), 500


@app.route('/get/novel')
def get_novel():
    try:
        returninfo = []
        conn = sqlite3.connect('./data/main.db')
        c = conn.cursor()
        cursor = c.execute('SELECT * FROM MAIN')
        for cur in cursor:
            try:
                if len(cur[3]) == 0:
                    return returninfo
            except TypeError:
                return returninfo
            else:
                conn = sqlite3.connect('./data/main.db')
                c = conn.cursor()
                cursor = c.execute("select * from MAIN limit 1;")
                for row in cursor:
                    NovelID = row[3].split(',')
                for nid in NovelID:
                    with open(f'data/novel/{nid}/info.yml', 'r', encoding='utf-8') as f:
                        y = yaml.safe_load(f)
                        ctime = time.strftime("%Y/%m/%d %H:%M", time.localtime(y['CreateTime']))
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
                        returninfo.append(
                            {'id': nid, 'title': y['title'], 'about': y['about'], 'CreateTime': ctime, 'allChapter': ac,
                             'allText': alltext_o})
                return returninfo

    except Exception as e:
        print(f"出现异常:{e}")
        return jsonify({'PythonErrorInfo': str(e)}), 500


@app.route('/get/idea')
def get_idea():
    try:
        returninfo = []
        conn = sqlite3.connect('./data/idea.db')
        c = conn.cursor()
        cursor = c.execute('SELECT * FROM IDEA')
        for row in cursor:
            iid = row[0]
            title = row[1]
            text = row[2]
            label = row[3]
            createtime = time.strftime("%Y/%m/%d %H:%M", time.localtime(row[4]))
            returninfo.append({'id': iid, 'title': title, 'text': text, 'label': label, 'createtime': createtime})
        return returninfo
    except Exception as e:
        print(f"出现异常:{e}")
        return jsonify({'PythonErrorInfo': str(e)}), 500


@app.route('/create/idea', methods=['GET'])
def create_idea():
    try:
        title = request.args.get('title')
        text = request.args.get('text')
        label = request.args.get('label')
        if title is None or text is None or label is None:
            return jsonify({'APIErrorInfo': '缺少参数'}), 500
        conn = sqlite3.connect('./data/idea.db')
        id = random.randint(1234567890, 9876543210)
        cursor = conn.cursor()
        sql = "INSERT INTO IDEA (IdeaID,Title,Text,Label,CreateTime) VALUES (?, ?, ?, ?, ?)"
        data = (id, title, text, label, int(time.time()))
        cursor.execute(sql, data)
        conn.commit()
        return {'status': 'ok', 'id': id}
    except Exception as e:
        print(f"出现异常:{e}")
        return jsonify({'PythonErrorInfo': str(e)}), 500


@app.route('/create/novel', methods=['GET'])
def create_novel():
    try:
        FirstUse = ''
        novelid = random.randint(1234567890, 9876543210)
        novelid_b = ',' + str(novelid)
        title = request.args.get('title')
        about = request.args.get('about')
        tmp_exam = request.args.get('template_example')
        if title is None or about is None or about is None or tmp_exam is None:
            return jsonify({'APIErrorInfo': '缺少参数'}), 500
        os.makedirs(f'data/novel/{novelid}')
        os.makedirs(f'data/novel/{novelid}/chapter')
        os.makedirs(f'data/novel/{novelid}/settings')
        data = {'id': novelid, 'title': title, 'about': about, 'CreateTime': int(time.time())}
        with open(f'data/novel/{novelid}/info.yml', 'w', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)
            f.close()
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
        if tmp_exam == "True" :
            with open(f'data/novel/{novelid}/chapter/第一章 示例.txt', 'w', encoding='utf-8') as f:
                f.write("   这是一个示例,你可以自由编辑这里面的内容,或者把这个示例删掉")
                f.close()
            with open(f'data/novel/{novelid}/settings/示例.txt', 'w', encoding='utf-8') as f:
                f.write("   这是一个示例,这里可以写世界观,或者人设,你可以自由编辑这里面的内容,或者把这个示例删掉")
                f.close()
        return {'status': 'ok'}
    except Exception as e:
        print(f"出现异常:{e}")
        return jsonify({'PythonErrorInfo': str(e)}), 500


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
            return jsonify({'APIErrorInfo': '此ID不存在'}), 500
        # del sql
        c.execute(f"UPDATE MAIN set NovelID = '{data}' where ID=1")
        conn.commit()
        # del file
        shutil.rmtree(f'data/novel/{willdel}')
        return jsonify({'status': 'ok'})
    except Exception as e:
        print(f"出现异常:{e}")
        return jsonify({'PythonErrorInfo': str(e)}), 500


@app.route('/del/idea')
def del_idea():
    try:
        willdel = request.args.get('id')
        conn = sqlite3.connect('./data/idea.db')
        c = conn.cursor()
        c.execute(f'delete from IDEA where IdeaId={willdel}')
        conn.commit()
        return jsonify({'status': 'ok'})
    except Exception as e:
        print(f"出现异常:{e}")
        return jsonify({'PythonErrorInfo': str(e)}), 500


@app.route('/edit/idea')
def edit_idea():
    try:
        willedit = request.args.get('id')
        new_title = request.args.get('title')
        new_text = request.args.get('text')
        new_label = request.args.get('label')
        if willedit is None or new_title is None or new_text is None or new_label is None:
            return jsonify({'APIErrorInfo': '缺少参数'}), 500
        conn = sqlite3.connect('./data/idea.db')
        c = conn.cursor()
        c.execute("SELECT * FROM IDEA WHERE IdeaID=?", (willedit,))
        idea = c.fetchone()
        if idea:
            c.execute("UPDATE IDEA SET Title=?, Text=?, Label=? WHERE IdeaID=?",
                      (new_title, new_text, new_label, willedit))
            conn.commit()
            return jsonify({'status': 'ok'})
        else:
            return jsonify({'APIErrorInfo': '此ID不存在'}), 500
    except Exception as e:
        print(f"出现异常:{e}")
        return jsonify({'PythonErrorInfo': str(e)}), 500


if __name__ == "__main__":
    run_simple('localhost', 65371, app)
