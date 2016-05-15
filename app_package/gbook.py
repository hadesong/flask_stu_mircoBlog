#coding:utf-8


from flask import Flask , Blueprint , request , render_template

import sqlite3 , time 
gbook = Blueprint("gbooks" , __name__)



#留言
@gbook.route("/gbook" , methods = ['POST' , 'GET'])
def guest_book():
    conn = sqlite3.connect('app.db')

    sql_create_table = '''create table if not exists gbooks
    (id INTEGER PRIMARY KEY AUTOINCREMENT , nikename text(20) , gemail text(20) , gtext  text(50) , time int(20))'''
    conn.execute(sql_create_table)

    sql_sel = ''' select * from gbooks order by id desc;  '''
    cur_sel = conn.execute(sql_sel)     

    gbooks_list = []
    for x in cur_sel:
        gbooks_list.append(list(x))


    ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    if request.method == 'POST':
        name = request.form.get('gnickname')
        mail =  request.form.get('gemail')
        text =  request.form.get('gmessage')
        #conn = sqlite3.connect('app.db')
        sql_insert = '''
 insert into gbooks( nikename , gemail ,  gtext , time) values ("%s" , "%s" ,"%s" , "%s");
 '''%(name , mail , text , ti)
        conn.execute(sql_insert)
        conn.commit()
        sql_select = '''select * from gbooks order by id desc;'''
        cur = conn.execute(sql_select)
        gbooks_list = []
        for row in cur:
            gbooks_list.append(row)
        conn.close()

    return render_template('gbooks.html' ,list=gbooks_list)


