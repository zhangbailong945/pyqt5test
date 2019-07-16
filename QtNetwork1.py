from PyQt5.QtCore import Qt,QUrl,QJsonDocument,QByteArray,QJsonParseError,pyqtSignal
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import *
from PyQt5.QtNetwork import QNetworkAccessManager,QNetworkRequest,QNetworkReply
import sys,json


class MyHttp(object):

    getResponse=pyqtSignal(str)
    
    def __init__(self,url,*args,**kwargs):
        super(MyHttp,self).__init__(*args,**kwargs)
        self._url=url
        
    
    def request(self):
        req=QNetworkRequest(QUrl(self.url))
        req.setRawHeader(b'Accept',b'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
        req.setRawHeader(b'Accept-Encoding',b'gzip, deflate, br')
        req.setRawHeader(b'ccept-Language',b'zh-CN,zh;q=0.9')
        req.setRawHeader(b'User-Agent',b'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')
        req.setHeader(QNetworkRequest.ContentTypeHeader,"application/json")
        self.nam=QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(req)

    def handleResponse(self,reply):
        err=reply.error()
        if err==QNetworkReply.NoError:
            bytes_string=reply.readAll()
            json_str=str(bytes_string,'utf-8')
            self.getResponse.emit(json_str)
        else:
            print("Error occurred:",err)
            print(reply.errorString())

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self,value):
        self._url=value

if __name__ == "__main__":
    app=QApplication(sys.argv)
    myHttp=MyHttp(url='http://localhost:8000/api/post/?format=json')
    sys.exit(app.exec_())
