# Chibrary

Chibrary是一个电子书（主要是epub）上传、下载、共享、评价网站。

网址（暂时设置为）:[网址](http://chibrary.chiro.work/)

## 项目结构

- Chibrary: 本网站的Python后端
- ChibraryEditor: Epub手动编辑器(可能用Calibre代替)
- ChibraryLocal: 网站的本地程序版本(实际上就是Chibrary的EXE封装)
- ChibraryWeb: 网站的前端页面
- ChibraryMobile: 手机APP

## 目标功能

- 网页
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
        - tag分类
        - 网站评论或者嵌入聊天室
        - 分享书籍
        - 心愿单

- 本地程序
    - （上述网页版功能）
    - 本地书库
    - 格式转换
    - 内置编辑器

- Epub编辑器
    - 导入书籍
    - 简单修改一些页面
    - 批量修改页面
    - 保存书籍

- 手机APP
    - （基本上是网站的封装）
    - 下载管理（会有吗）
    - 本地书籍管理（会有吗）