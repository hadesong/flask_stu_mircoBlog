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
    port = sae.const.MYSQL_PORT
    string = db+"\n"+user+"\n"+pw+"\n"+host+"\n"+str(port)
    try:
        database = MySQLdb.connection(host=host , user=user , passwd=pw , db=db ,  port=port)
        cur = database.cursor()
        sql = '''
        select * from test;
        '''
        cur.execut(sql)
        database.commit()
    except Exception, e:
        return "error%s"%e+"<br>%s"%string



    return string

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=44444 , debug=True)