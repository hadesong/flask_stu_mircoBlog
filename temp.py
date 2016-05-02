#coding:utf-8
from flask import Flask , render_template , g , request
import random
import time
import MySQLdb

app = Flask(__name__)

@app.route('/db')
def db():
    db = "app_moxx"
    user = "yl15y5jjjy"
    pw = "ixkw44lxjw403h1330m34yykl3zjxzi243k0mxzk"
    host = "10.67.15.120"
    port = 3307
    string = db+"\n"+user+"\n"+pw+"\n"+host+"\n"+str(port)
    try:
        database = MySQLdb.connect(host , user , pw  ,db )
        cur = database.cursor()
        sql = '''
        select * from test;
        '''
        cur.execut(sql)
        database.commit()
    except Exception, e:
        print "error%s"%e+"<br>%s"%string



    print string

if __name__ == '__main__':
    #app.run(host='0.0.0.0' , port=44444 , debug=True)
    db()