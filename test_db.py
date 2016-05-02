#coding:utf-8
from flask import Flask , render_template , g , request
import random
import time
import MySQLdb
import sae.const

app = Flask(__name__)

@app.route('/db')
def db():
	info = ''
	try:
		db = MySQLdb.connect(sae.const.MYSQL_HOST,sae.const.MYSQL_USER, sae.const.MYSQL_PASS , sae.const.MYSQL_DB)
		info = 'connect_seccess'
	except Exception, e:
		info = 'connect_fail'

	cur = db.cursor()
	sql = '''
	create table test(num int , time int);
	insert into test (num , time) values ('1234567' , %s);

	'''%(time.time)
	cur.execut(sql)
	db.commit()
	return "test_db" + info


if __name__ == '__main__':
	app.run(host='0.0.0.0' , port=45324 , debug=True)