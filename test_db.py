#coding:utf-8
from flask import Flask , render_template , g , request
import random
import time
import MySQLdb


app = Flask(__name__)

@app.route('/db')
def db():
	info = ''
	try:
		db = MySQLdb.connect('SAE_MYSQL_HOST_M' , 'SAE_MYSQL_USER' , 'SAE_MYSQL_PASS' , 'app_moxx')
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