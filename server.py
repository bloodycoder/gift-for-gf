#coding=utf-8 
from wsgiref.simple_server import make_server
from app import application
port = 80
httpd = make_server('', port, application)
print "Serving HTTP on port "+str(port)+"..."
httpd.serve_forever()
