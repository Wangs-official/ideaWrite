import os
import sqlite3
import time

if os.path.exists("install.lock"):
    print("已初始化过")
    exit()

f = open('data/main.db', 'w')
f.close()
f = open('data/idea.db', 'w')
f.close()

print("将会在ideaWrite的目录下放置数据库")
conn = sqlite3.connect('./data/main.db')
c = conn.cursor()
c.execute('''CREATE TABLE MAIN
       (ID INT PRIMARY KEY     NOT NULL,
       JoinTime           INT,
       LastLogin           INT,
       NovelID           TEXT,
       AllText        INT);''')
c.execute(f"INSERT INTO MAIN (ID,JoinTime,LastLogin,NovelID,AllText) \
      VALUES (1,{int(time.time())},{int(time.time())},'',0)")
print("主数据库创建成功")
conn.commit()
conn.close()

conn = sqlite3.connect('./data/idea.db')
c = conn.cursor()
c.execute('''CREATE TABLE IDEA
       (IdeaID INT PRIMARY KEY     NOT NULL,
       Title           TEXT,
       Text            TEXT,
       Label        TEXT,
       CreateTime         INT);''')
print("灵感数据库创建成功")
conn.commit()
conn.close()

import yaml

f = open("data/settings/settings.yml", "w")
data = {'editor': [{'text_size': 14, 'editor_background': '', 'editor_bg_opacity': 0, 'autosave': '60'}],
        'cloud_sync': [{'enable': False}]}
with open('data/settings/settings.yml', 'w', encoding='utf-8') as f:
    yaml.dump(data=data, stream=f, allow_unicode=True)
print("生成设置文件完成")
f.close()

f = open("data/settings/cloud_sync.yml", "w")
data = {'webDav': [], 'aliyun_pan': []}
with open('data/settings/cloud_sync.yml', 'w', encoding='utf-8') as f:
    yaml.dump(data=data, stream=f, allow_unicode=True)
print("生成云同步文件完成")
f.close()

os.makedirs('data/novel')

f = open("install.lock", 'w')
f.close()

print('初始化完成')
