#coding:utf-8
from flask import Flask , render_template , g , request
import random
import time
import MySQLdb

app = Flask(__name__)

@app.route('/db')
def db():
    db = 'test'
    user = 'root'
    pw = '111111'
    host = 'localhost'
    port = 3307
    string = db+"\n"+user+"\n"+pw+"\n"+host+"\n"+str(port)
    try:
        import sae.const
        db = sae.const.MYSQL_DB
        user = sae.const.MYSQL_USER
        pw = sae.const.MYSQL_PASS
        host = sae.const.MYSQL_HOST
        port = int(sae.const.MYSQL_PORT)
        string = db+"\n"+user+"\n"+pw+"\n"+host+"\n"+str(port)
    except Exception, e:
        pass
    try:
        conn = MySQLdb.connect(host=host , user=user , passwd=pw  , db=db)
        cursor = conn.cursor()
        # 使用execute方法执行SQL语句
        v = cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchall()
        sql = "select * from test ;"
        cursor.execute(sql)
        res  = cursor.fetchall()
        #sel1 = """insert into test(num ,  time) values ("2342" , "2222222222")"""
        
       # info = []
       # for x in cursor.fetchall():
       #     info.append(x)


#        conn.select_db(db)
#        sql = "select * from test ;"
#        conn.query(sql)
#        rec = conn.store_result()
#        res = rec.fetch_row()

        return str(res) + str(v) + sql
    except Exception, e:
        return "error%s"%e+"<br>%s"%string
    return "ddddddddddd<br>"+string




if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=44444 , debug=True)