#coding:utf-8
from app_package import app
from flask import render_template , request , g , Response , make_response , redirect
import sqlite3 , time 
import cgi ##转义html代码
import HTMLParser #发转html
from gbook import gbook
from admin import admin
import urllib , hashlib


# gbook 蓝图
app.register_blueprint(gbook)
# admin 蓝图 
app.register_blueprint(admin)

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/')
@app.route('/index')
def index():
    conn = sqlite3.connect('app.db')
    sql_sel = ''' select * from posts order by id desc;  '''
    cur_sel = conn.execute(sql_sel)     

    posts_list = []
    for x in cur_sel:
        posts_list.append(list(x))
    return render_template('index.html'  , list=posts_list )


@app.route('/tags')
def tags():
    return render_template('tags.html' )


#登录
# 若cookies 存在且 账号密码正确 ,则重定向至管理页面
# 判断表单字段啊是否正确并重定向
@app.route('/login' , methods=['POST' , 'GET'])
def login():
    login_msg = None
    if 'user' and 'pawd' in request.cookies :
        if request.cookies['user']==app.config['USERNAME'] and request.cookies['pawd']==app.config['PASSWORD']:
            return redirect('/admin' )
    if request.method == 'POST':
        user = request.form['username']
        pawd = hashlib.md5(request.form['password']).hexdigest()
        if user != app.config['USERNAME']:
            login_msg =  'Error Username!'
        elif pawd != app.config['PASSWORD']:
            login_msg = 'Error Password!'
        else:
            login_msg = 'Seuccessfully!!'
            rsp = make_response(redirect('/admin'))
            rsp.set_cookie('user' , user)
            rsp.set_cookie('pawd' , pawd)
            return  rsp
    return render_template('login.html' , login_msg=login_msg)




#添加文章
@app.route('/add' , methods=['POST' , 'GET'])
def add():
    return render_template('admin.html')

#修改文章
@app.route('/modify/<id>' , methods=['POST' , 'GET'])
def modify(id):
    id = int(id)
    conn=sqlite3.connect('app.db')
    sql = '''select * from posts where id=%d; '''%id
    cur = conn.execute(sql)
    post_text = []
    for x in cur:
        post_text.append(x)

    ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    if request.method=='POST':
        title = request.form.get('title')
        post =  request.form.get('post')
        sql_update = '''
        update posts set title = "%s" , post = "%s" , time="%s" where id = %s
        '''%(title , post , ti , id)
        conn.execute(sql_update)
        conn.commit()
        return redirect('/admin')
        #return sql_update
    if post_text:
        return render_template('modify.html' , text=post_text)
    else:
        return redirect(404)


#删除文章
@app.route('/delete/<id>' , methods=['POST' , 'GET'])
def delet(id):
    id = int(id)
    conn = sqlite3.connect('app.db')
    cur = conn.execute("select id , title from posts where id=%d;"%id )
    title_text =[]
    for x in cur:
        title_text.append(x)

    if request.method == 'POST':
        sql = "delete from posts where id=%d;"%id
        conn.execute(sql)
        conn.commit()
        return redirect('/admin')
        #return sql

    if title_text:
        return  render_template('delete.html' , text  = title_text)
    else:
        return redirect(404)


#文章页面
@app.route('/post/<id>' , methods=['POST' , 'GET'])
def post(id):
    id = int(id)
    conn = sqlite3.connect('app.db')
    sql = '''select * from posts where id=%d;'''%id
    cur = conn.execute(sql)
    post_text = []
    for x in cur:
        post_text.append(x)
    if post_text:
        return  render_template('post.html' , text  = post_text)
    else:
        return redirect(404)


    #return sql




















