#coding:utf-8


from app_package import app
from flask import Flask , Blueprint , request , render_template , redirect

import sqlite3 , time 
admin = Blueprint("admini" , __name__)



#管理后台
@admin.route("/admin" , methods = ['POST' , 'GET'])
def admin_manage():
    if 'user' and 'pawd' in request.cookies :
        if request.cookies['user']==app.config['USERNAME'] and request.cookies['pawd']==app.config['PASSWORD']:


            conn = sqlite3.connect('app.db')
            sql_create_table = '''create table if not exists posts
            (id INTEGER PRIMARY KEY AUTOINCREMENT , title text , post text ,  time int(20))'''
            conn.execute(sql_create_table)
            sql_select = '''select * from posts order by id DESC; '''
            cur_ord = conn.execute(sql_select)
            post_list = []
            for x in cur_ord:
                post_list.append(list(x))

            ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            if request.method=='POST':
                title = request.form.get('title')
                post =  request.form.get('post')
                sql_inster = '''
insert into posts (title , post ,  time) values ("%s" , "%s" ,  "%s");
                '''%(title , post , ti)
                conn.execute(sql_inster)
                conn.commit()

                sql_select = '''select * from posts order by id DESC; '''
                cur_ord = conn.execute(sql_select)
                post_list = []
                for x in cur_ord:
                    post_list.append(list(x))
                return render_template('admin.html' , list=post_list )



            return render_template('admin.html' , list=post_list )

    else:
        return redirect('/index')


