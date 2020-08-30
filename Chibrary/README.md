# Chibrary 后端

## 计划功能和TODO

- 基础功能
    - 用户系统
    - 上传
    - 下载
    - 自动更新
    - 搜索书籍
- 扩展功能
    - 书评系统
        - 评论
        - 评分
    - 书架
    - 推书
    - tag分类
    - 网站评论或者嵌入聊天室
    - 分享书籍
    - 心愿单
    - 添加书源

## 可行性验证

## 技术难点记录

### 数据库设计

还是使用MongoDB。

---------

**基本功能**

- user
    - username
    - password
    - info
        - createdAt (float, 表示秒数)
        - lastLogin (0表示没有登录过)
        - level: 1 (1普通游客)
        - birthday
        - gender (性别)
        - head (url)
        - status: normal/banned
    - statistics (统计数据)
        - upload
        - download
        - comments
        - wishes
        - recommends

*token* 是登录后生成的通行码
- token
    - token
    - username

- bookSource
    - name
    - info
        - createdAt
        - description
        - author
        - nick

- book
    - name
    - bid(_id) (本站)(主键)
    - sources: dict
        - name (wenku8 or dmzj or...)
        - args (用来调取书源的参数)
            - key
            - ...
        - data
            - lastUpdate (更新时间)
            - update (更新内容)
    - info
        - name(*)
        - description(*)
        - author(*)
        - stars (*)(评分，Float，5 max)
        - bid
        - cover
        - createdAt
        - lastUpdate
        - starCount (评分人数)
    - tags: list

----------

**拓展功能**

- tag
    - tag
    - bid

- comments
    - bid
    - username
    - createdAt
    - content
        - type: text/html/md
        - data

- bookshelves (书架(散装))
    - username
    - bid

- wishes (心愿单)
    - username
    - bid

- recommends
    - username
    - bid
    

### 接口设计

**返回格式**
```json
{
"code": 0,
"message": "Success",
"data": {
  "token": "___",
  "searchResult": {
    "data": [],
    "page": 1
  },
  "userInfo": {
    "username": "username",
    "...": "..."
  },
  "bookInfo": {
    "...": "..."
  },
  "bookSource": {
    "...": "..."
  },
  "download": {
    "url": "...",
    "filename": "..."
  }
}
}
```

- /api_v1 *API和动态网页的内容由nginx重定向到server*
    - /user
        - /login: {username, password(前端就sha1加密一次), captcha}
            - =>token
        - /logout: {token}
        - /register: {username, password(前端就sha1加密一次), captcha}
        - /info: {username}
        - /updateInfo: {...}
    
    - /book
        - /add: {name, author, description}
        - /upload: {@token, bid, src: {name, data: {update, }}}
        - /download/<name>: {bid, key}
        - /addSource/<name>: {bid, key}
        - /search: {}
    
    - /search: {query, type: book/user, page=1, limit=20}
    
    - /bookSource
        - /add: {name, author, description, nick} @token
        - /search: {keyword}
        - /find: {name}
        - /delete: {name} @token
*这部分可以重定向到腾讯云做纯前端处理*
- /user
    - /{username} => 用户主页
- /book
    - /{bid} => 书籍主页
*后面静态的东西重定向到腾讯云*
- /apps
