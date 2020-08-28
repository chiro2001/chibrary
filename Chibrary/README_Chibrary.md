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

**基本功能**

- user
    - username
    - password
    - info
        - createdAt
        - lastLogin
        - birthday
        - gender (性别)
        - head (url)
    - statistics (统计数据)
        - upload
        - download
        - comments
        - wishes
        - recommends

- book
    - name
    - bid(_id) (本站)(主键)
    - src: dict (name(wenku8 or dmzj or...))
        - args (用来调取书源的参数)
            - bid
            - ...
        - data
            - lastUpdate (更新时间)
            - update (更新内容)
    - info
        - name
        - bid
        - cover
        - author
        - createdAt
        - lastUpdate
        - description
    - tags: list

----------

**拓展功能**

- tag2book (双向查询，数据冗余一下)
    - tag: dict
        - bid

### 接口设计

