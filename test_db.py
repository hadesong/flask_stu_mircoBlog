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
    string = db+user+pw+host+port
    return string
	#db = MySQLdb.connect(HOST_M  , USER , PASS , DB)
	#cur = db.cursor()
	#sql = '''
	#select * from test;
	#'''
	#cur.execut(sql)
	##db.commit()


if __name__ == '__main__':
	app.run(host='0.0.0.0' , port=44444 , debug=True)