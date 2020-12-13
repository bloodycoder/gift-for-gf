#coding=utf-8 
# -*- coding:cp936 -*-
import re
import urls
from cgi import parse_qs
class application:
    """
    造轮子计划1073(a clean python web frame):
    使用方法
    常量:self.method,用来判断是post,get
    内置的几个方法:getTemplate,getPost
    如果要访问数据库,
    Model.build_connect 
    Model.exec_ins()
    Model.close()
    """
    def __init__(self,environ,start_response):
        self.environ = environ
        self.start = start_response
        self.status = '200 OK'
        self.response_headers = [('Content-type','text/html')]
        self.urls = urls.urls
    def __iter__(self):
        self.method = self.environ['REQUEST_METHOD']
        content = self.getPage()
        self.start(self.status,self.response_headers)
        yield content
    def getPage(self):
        path = self.environ['PATH_INFO']
        for pattern in self.urls:
            m = re.match(pattern[0],path)
            if m:
                function = getattr(self,pattern[1])
                return function()
        return '404 not found'
    def getTemplate(self,tem_name,rep=0):
        #这个函数返回内容,tem_name是文件名字
        #参数rep是一个字典，默认为0
        f = open('template/'+tem_name)
        html = f.read()
        if(rep!=0):
            for to_replace in rep:
                strinfo = re.compile('\{\%\s*'+str(to_replace)+'\s*\%\}')
                html = strinfo.sub(rep[to_replace],html)
        return html
    def getPost(self,itemList):
        if(self.environ['REQUEST_METHOD'] == 'POST'):
            request_body_size = int(self.environ.get('CONTENT_LENGTH', 0))
            request_body = self.environ['wsgi.input'].read(request_body_size)
            d = parse_qs(request_body)
            if(len(d) == 0):
                return -1
            ans = []
            for item in itemList:
                ans.append(d.get(item,[])[0].strip())
            return ans
    """
    *********************************************
    *add your function here.                    *
    *For example                                *
    *def func_index(self):                      *
    *    self.status = '200 OK'                 *
    *    return self.getTemplate('about_me.htm')*
    *********************************************
    """
    def welcome_01(self):
        self.status = '200 OK'
        if(self.method == 'GET'):
            return self.getTemplate('welcome01.html',{'error':' '})
        elif(self.method == 'POST'):
            postInfo = self.getPost(['phonenum'])
            phoneNum = postInfo[0]
            if(phoneNum == '13122152186'):
                return self.getTemplate('successPage.html',{
                    'link':'<a href="/ballweight/" target="_blank" rel="noopener noreferrer">Next Problem</a>',
                    'successWords':'<h3 id="my-hobbies:6083a88ee3411b0d17ce02d738f69d47">Congratulations</h3> \
                    <p>you success finished the your first problem.</p> \
                    <p>click the linked above to continue.</p>'
                    })
            return self.getTemplate('welcome01.html',{'error':'<p style="color: #F5222D;">oops,please try again</p>'})
    def problem_01(self):
        self.status = '200 OK'
        if(self.method == 'GET'):
            return self.getTemplate('problem1.html',{'error':' '})
        elif(self.method == 'POST'):
            postInfo = self.getPost(['tryTimes','firstTry'])
            tryTimes = postInfo[0]
            firstTry = postInfo[1]
            errorPage = self.getTemplate('problem1.html',{'error':'<p style="color: #F5222D;">oops,please try again</p>'})
            if(tryTimes == '2'):
                firstTry = firstTry.split(' ')
                if(len(firstTry) == 2 and firstTry[0] == '3' and firstTry[1] == '3'):
                    return self.getTemplate('successPage.html',{
                        'link':'<a href="/birthdayProblem/" target="_blank" rel="noopener noreferrer">Next Problem</a>',
                        'successWords':'<h3 id="my-hobbies:6083a88ee3411b0d17ce02d738f69d47">Congratulations</h3> \
                        <p>You are really brilliant! It is easy to get your gift. </p> \
                        <p>click the linked above to continue.</p>'
                        })
            return errorPage
    def problem_02(self):
        self.status = '200 OK'
        if(self.method == 'GET'):
            return self.getTemplate('problem2.html',{'error':' '})
        elif(self.method == 'POST'):
            postInfo = self.getPost(['peopleCnt'])
            peopleCnt = postInfo[0]
            errorPage = self.getTemplate('problem2.html',{'error':'<p style="color: #F5222D;">oops,please try again</p>'})
            if(peopleCnt == '5'):
                return self.getTemplate('successPage.html',{
                        'link':'<a href="/poem/" target="_blank" rel="noopener noreferrer">Next Problem</a>',
                        'successWords':'<h3 id="my-hobbies:6083a88ee3411b0d17ce02d738f69d47">Congratulations</h3> \
                        <p>You are really brilliant! It is easy to get your gift. </p> \
                        <p>click the linked above to continue.</p>'
                        })
            return errorPage
    def problem_03(self):
        self.status = '200 OK'
        if(self.method == 'GET'):
            return self.getTemplate('problem3.html',{'error':' '})
        elif(self.method == 'POST'):
            postInfo = self.getPost(['originPoem'])
            poem = postInfo[0]
            errorPage = self.getTemplate('problem3.html',{'error':'<p style="color: #F5222D;">oops,please try again</p>'})
            if(poem.find('forever')!=-1 and poem.find('world')!=-1 and poem.find('moon')!=-1):
                return self.getTemplate('successPage.html',{
                        'link':'<a href="https://www.yuque.com/docs/share/7a63076e-56fe-4a8c-b025-4eee68626333" target="_blank" rel="noopener noreferrer">How to get Gift</a>',
                        'successWords':'<h3 id="my-hobbies:6083a88ee3411b0d17ce02d738f69d47">Congratulations</h3> \
                        <p>You are really brilliant!You pass the final exam. It is easy to get your gift. </p> \
                        <p>click the linked above to get your gift.</p>'
                        })
            return errorPage