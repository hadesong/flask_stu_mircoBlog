#coding:utf-8
from flask import Flask , render_template , g , request
import random
import time
import MySQLdb
import sae.const

app = Flask(__name__)

@app.route('/db')
def db():
	DB = sae.const.MYSQL_DB 
	USER = sae.const.MYSQL_USER 
	PASS = sae.const.MYSQL_PASS 
	HOST_M = sae.const.MYSQL_HOST 
	HOST_S = sae.const.MYSQL_HOST_S 
	PORT = int(sae.const.MYSQL_PORT)

	db = MySQLdb.connect(HOST_M , PORT , USER , PASS , DB)

	cur = db.cursor()
	sql = '''
	select * from test;

	'''
	cur.execut(sql)
	#db.commit()
	return sql


if __name__ == '__main__':
	app.run(host='0.0.0.0' , port=45324 , debug=True)