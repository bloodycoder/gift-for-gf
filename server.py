#coding=utf-8 
from wsgiref.simple_server import make_server
from app import application
httpd = make_server('', 80, application)
print "Serving HTTP on port 8000..."
httpd.serve_forever()
