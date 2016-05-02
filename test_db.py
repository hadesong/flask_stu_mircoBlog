#coding:utf-8
from flask import Flask , render_template , g , request
import random
import time
import MySQLdb

app = Flask(__name__)

@app.route('/db')
def db():
	DB = SAE_MYSQL_DB 
	USER = SAE_MYSQL_USER 
	PASS = SAE_MYSQL_PASS 
	HOST_M = SAE_MYSQL_HOST 
	HOST_S = SAE_MYSQL_HOST_S 
	PORT = int(SAE_MYSQL_PORT)

	#db = MySQLdb.connect(HOST_M  , USER , PASS , DB)
	#cur = db.cursor()
	#sql = '''
	#select * from test;
	#'''
	#cur.execut(sql)
	##db.commit()
	return DB+USER+PASS+HOST_M+PORT


if __name__ == '__main__':
	app.run()