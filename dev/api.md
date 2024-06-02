# 内嵌API
**一些在前端需要请求的API**

您可以打开 `app/ideaWrite.api.py` 自行更改或查看

全局域名均为`http://localhost:65371`,请求方式均为`GET`

## 错误捕获

您可以在前端设置发生`500`状态码后的行动,API在遇到错误时(无论是API错误还是Python错误),都会返回带有500状态码的数据

- 示例:

    ```json
    {"PythonErrorInfo":"File Not Found"} (Python错误)
    {"APIErrorInfo":"此ID不存在"} (API错误)
    ```

## 初始化

1. `/start`

    - 参数: 无

    - 用途: 用于刷新最后一次登录时间

    - 返回值示例:`{"LastLogin":(时间戳)}`

## 获取类

1. `/get/novel`

    - 参数: 无

    - 用途: 用于获取小说列表

    - 返回值示例

    ```json
    状态码200:

    [
        {
            "CreateTime": "1970/01/01 8:00:00",
            "about": "这是一个测试小说，如你所见，是真的",
            "allChapter": 0,
            "allText": 0,
            "id": "100000",
            "title": "测试小说"
        }
    ]

    状态码404(无小说):

    {"novel": ""}
    ```

## 文件创建/删除

1. `/create/novel`

    - 参数: `?id={小说ID}&title={标题}&about={描述}`

    - 用途: 创建小说

    - 返回值示例:`{"status":"ok"}`

2. `/del/novel`

    - 参数: `?id={小说ID}`

    - 用途: 删除小说

    - 返回值示例:`{"status":"ok"}`