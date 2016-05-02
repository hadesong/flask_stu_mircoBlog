#coding:utf-8
from flask import Flask , render_template , g , request
import random
import time
import MySQLdb
import sae.const

app = Flask(__name__)

@app.route('/db')
def db():
    db = sae.const.MYSQL_DB
    user = sae.const.MYSQL_USER
    pw = sae.const.MYSQL_PASS
    host = sae.const.MYSQL_HOST
    port = int(sae.const.MYSQL_PORT)
    string = db+"\n"+user+"\n"+pw+"\n"+host+"\n"+str(port)
    try:
        conn = MySQLdb.connect(host=host , user=user , passwd=pw ,  port=port)
        cursor = conn.cursor()
        # 使用execute方法执行SQL语句
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchall()
        sql = "use  %s ; select * from test ;"%db
        cursor.execute(sql)
        res  = cursor.fetchall():
        info = []
        for x in res:
            num =  x[0]
            time = x[1]
            info.append(num+time)
        
       # info = []
       # for x in cursor.fetchall():
       #     info.append(x)


#        conn.select_db(db)
#        sql = "select * from test ;"
#        conn.query(sql)
#        rec = conn.store_result()
#        res = rec.fetch_row()

    except Exception, e:
        return "error%s"%e+"<br>%s"%string



    return str(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=44444 , debug=True)