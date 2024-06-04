# ideaWrite 灵感写
**一款完全免费开源的本地小说编辑器**

## 💡 简介

ideaWrite灵感写是一款完全免费开源的本地小说编辑器,使用Flask作为后端,90%后端渲染

很多写小说软件都收费,但收费的都是基本功能,我的想法就是做出一个完全免费而且具有很多功能的小说软件

## 💻 使用

- 从0开始启动

    如果你是一个可可爱爱的小白,根本不会什么Python安装和执行啊,那你可以跟着下方教程来启动ideaWrite

    1.0 万物之源

    Windows用户自行 **https://bing.com** 搜索 **Python安装教程**


    1.1 安装传奇Git软件

    **MacOS用户请忽略此步骤**

    不多介绍,请 [点击这里](https://github.com/git-for-windows/git/releases/download/v2.45.1.windows.1/Git-2.45.1-64-bit.exe) 下载最新版的Git,然后正常走流程安装即可,如果你不会安装,请打开 **https://bing.com** 搜索 **Windows如何安装Git**

    1.2 拉库

    Windows用户请打开 **命令提示符** (win+r 输入 cmd) , MacOS用户请打开 **终端** (启动台直接搜索)

    > 推荐Windows用户建一个文件夹在哪个地方,然后打开文件夹,右键打开命令提示符,因为Windows的cd有点魔幻,可能过不去

    打开后,输入这串指令 `git clone https://github.com/Wangs-official/ideaWrite.git`(如果想在某个文件夹下clone,请`cd 文件夹路径`)

    > 如果显示TimeOut什么的,请运行这个指令 `git clone https://kkgithub.com/Wangs-official/ideaWrite.git` 原理是国内镜像

    ![](https://s3.bmp.ovh/imgs/2024/05/28/7b8fb32a608af02e.png)

    1.3 安装库
    
    还是那个终端,执行这个指令 `pip3 install -r requirements.txt -i https://pypi.douban.com/simple`

    ![](https://s3.bmp.ovh/imgs/2024/05/29/c4f4a63e8536b154.png)

    1.4 设置

    启动前需要进行一次初始化,请您输入以下指令(逐行输入)

    ```bash
    cd app
    python3 setup.py
    ```

    ![](https://s3.bmp.ovh/imgs/2024/05/29/51f7369092d38f35.png)

    完成后即可继续

    1.5 启动

    请您再打开一个**命令提示符/终端**,第二个终端执行`cd {项目文件夹/app}`

    然后在第一个**命令提示符/终端**输入 `python3 ideaWrite.api.py`

    最后在第二个**命令提示符/终端**输入 `python3 ideaWrite.app.py`

    成功后,应该会显示这样的结果

    ```
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://localhost:65371
    ```

    ![](https://s3.bmp.ovh/imgs/2024/05/29/44a346b02ba825ab.png)

    如果两个**命令提示符/终端**都显示了以上的信息(除最后一行,一个是 **http://localhost:65370** ,一个是 **http://localhost:65371** )那么恭喜你,启动成功了

    打开浏览器,在地址栏输入`http://localhost:65530`就可以愉快的使用了~

    > 请注意,如果要关闭它们,请在窗口处按下键盘上的 `Ctrl` 和  `C` 按钮(也就是复制的快捷键),直接关闭窗口会导致端口无法释放,下次启动时需要手动释放端口

- 故障排除

    1. 端口占用

    ```
    Address already in use
    Port 65371 is in use by another program. Either identify and stop that program, or start the server with a different port.
    ```

    这种情况一般是**直接关闭窗口**导致的,如果你是MacOS请在**终端**输入以下指令

    ```bash
    lsof -i :65371 (或者是63370)

    执行后可能会显示:
    COMMAND   PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    Python  71730  mac    4u  IPv4 0x45c58121018e1cc7      0t0  TCP localhost:65371 (LISTEN)

    看第二个PID,然后执行

    kill -9 {刚才那个PID}
    例如这个: kill -9 71730
    ```

    2. 开启顺序不对

    ```
    Traceback (most recent call last):
    File "/xxx/ideaWrite/app/ideaWrite.app.py", line 17, in <module>
        def index_page(LTime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(json.loads(requests.get(f'{api_url}/start').text)['LastLogin'])),NovelInfo='0'):
    File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/json/__init__.py", line 346, in loads
        return _default_decoder.decode(s)
    File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/json/decoder.py", line 337, in decode
        obj, end = self.raw_decode(s, idx=_w(s, 0).end())
    File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/json/decoder.py", line 355, in raw_decode
        raise JSONDecodeError("Expecting value", s, err.value) from None
    json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    ```

    请先开启**ideaWrite.api.py**后再开启**ideaWrite.app.py**

    

    

        

    

    





    
