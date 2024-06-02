# 文件结构
**乱糟糟**

```
ideaWrite
    - app/ (运行ideaWrite必须的文件)
        -- data/ (存储数据的地方)
            --- novel/ (小说文件)
                ---- (小说ID)/
                    ----- chapter/ (小说章节)
                    ----- settings/ (小说设定(世界观等))
                    ----- info.yml (小说信息)
            --- settings.yml/
                ---- cloud_sync.yml (云同步设置文件)
                ---- settings.yml (设置文件)
            --- idea.db (灵感存储数据库)
            --- main.db (主数据库)
        -- static/
            --- css/ (CSS文件)
            --- js/ (JS文件)
            --- templates/ (模版文件)
        -- ideaWrite.api.py (ideaWrite API脚本)
        -- ideaWrite.app.py (ideaWrite APP脚本)
        -- setup.py (安装器)
        -- install.lock (安装锁定)
    - dev/ (开发文档)
    - .gitignore (都知道是什么吧)
    - LICENSE (MIT许可证)
    - version.json (版本号文件)
```