from flask import Flask , render_template , g , request
import random
import time
import MySQLdb


app = Flask(__name__)

@app.route('/db')
def db():
	return "test_db"


if __name__ == '__main__':
	app.run(host='0.0.0.0' , port=45324 , debug=True)