#coding:utf-8
import sae
#sae.add_vendor_dir('Lib/site-packages/lxml.egg/lxml')
from test_db import app
application = sae.create_wsgi_app(app)
