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

1. `/get/novel` (无小说时,直接返回空列表)

   - 参数: 无

   - 用途: 用于获取小说列表

   - 返回值示例

   ```json
   [
       {
           "CreateTime": "1970/01/01 8:00",
           "about": "这是一个测试小说，如你所见，是真的",
           "allChapter": 0,
           "allText": 0,
           "id": "100000",
           "title": "测试小说"
       }
   ]
   ```

   |     键     |    值    |  类型  |
   | :--------: | :------: | :----: |
   | CreateTime | 创建时间 | string |
   |   about    | 小说描述 | string |
   | allChapter |  总章节  |  int   |
   |  allText   |  总字数  |  int   |
   |     id     |  小说ID  | string |
   |   title    | 小说标题 | string |


2. `/get/idea` (无灵感时,直接返回空列表)

   - 参数: 无

   - 用途: 用于获取灵感列表

   - 返回值示例

   ```json
   [
       {
           "createtime": "1970/01/01 8:00",
           "id": 1000000000,
           "label": "灵感",
           "text": "这是一个测试的灵感",
           "title": "测试"
       }
   ]
   ```

   |     键     |    值    |  类型  |
   | :--------: | :------: | :----: |
   | createtime | 创建时间 | string |
   |     id     |  灵感ID  |  int   |
   |   label    | 灵感标签 | string |
   |    text    | 灵感内容 | string |
   |   title    | 灵感标题 | string |
   

3. `/get/dashboard`

   - 参数: 无

   - 用途: 用于获取仪表盘内容

   - 返回值示例

   ```json
   {
        "All_Book": 0,
        "All_Text": 0,
        "All_Think": 0,
        "Use_Time_Day": 10
   }
   ```

   |      键      |     值     | 类型 |
   | :----------: | :--------: | :--: |
   |   All_Book   |  创建的书  | int  |
   |   All_Text   |   总字数   | int  |
   |  All_Think   | 记录的灵感 | int  |
   | Use_Time_Day |  使用天数  | int  |

   
## 文件创建/删除

1. `/create/novel`

   - 参数: `?id={小说ID}&title={标题}&about={描述}`

   - 用途: 创建小说

   - 返回值示例:`{"status":"ok"}`

2. `/create/idea`

   - 参数: `?title={标题}&text={内容}&label={标签}`

   - 用途: 创建灵感

   - 返回值示例:`{"status":"ok","id":"(10位数字)"}`

3. `/del/novel`

   - 参数: `?id={小说ID}`

   - 用途: 删除小说

   - 返回值示例:`{"status":"ok"}`

4. `/del/idea`

   - 参数: `?id={灵感ID}`

   - 用途: 删除灵感

   - 返回值示例:`{"status":"ok"}`