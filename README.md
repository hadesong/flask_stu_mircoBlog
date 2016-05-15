一个简单的博客系统.....

使用到:
    flask \ bootstrap \ sqlite \

功能:
    主页展示文章 , 每篇只显示前150字 , 点击文章名进入文章详情页

    标签页..没做 , 考虑通过搜索数据库关键词添加标签

    留言板 , 提供用户留言 , 最新留言在前 [[ 没有做表单验证 !! 有被注入风险 !!]]

    搜索框 . bootstrap 导航栏提供  ..没写action

    登录 ,  内设一组用户名密码 , 密码md5 加密 ,  若输入不正确有提示 , 若验证成功
        则进入/admin页面 并把用户名和加密后的密码写入cookies 

        再次点击登录  按钮  或直接进入 /admin 页面会进行cookies判断 , 验证成功进入
        /admin , 验证失败 进入登录页面或返回主页/index
        [[ 没有做表单验证 !! 有被注入风险 !!]]

D:.
│  app.db
│  config.py
│  README.md
│  run.py
│
└─app_package
    │  admin.py
    │  gbook.py
    │  views.py
    │  __init__.py
    │
    ├─static
    └─templates
            404.html
            500.html
            admin.html
            base.html
            delete.html
            gbooks.html
            index.html
            login.html
            modify.html
            post.html
            tags.html