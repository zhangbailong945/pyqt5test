from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QFont,QFontDatabase
from PyQt5.QtNetwork import QNetworkAccessManager,QNetworkRequest,QNetworkReply

import sys,json

class MyHttp(object):
    """docstring for ClassName."""
    def __init__(self, *arg,**kwargs):
        super(MyHttp, self).__init__(*arg,**kwargs)
    
    def request(self):
        req=QNetworkRequest(QUrl(self.url))
        req.setRawHeader(b"Accept",b"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
        req.setRawHeader(b"Accept-Encoding",b"gzip, deflate, br")
        req.setRawHeader(b"Accept-Language",b"zh-CN,zh;q=0.9")
        req.setRawHeader(b"User-Agent",b"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36")
        self.nam=QNetworkAccessManager()
        self.nam.finished.connect(self.response)
        self.nam.get(req)
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self,value):
        self._url=value
    
    def response(self,reply):
        er=reply.error()
        if er==QNetworkReply.NoError:
            bytes_string=reply.readAll()
            print(bytes_string)
        else:
            print("Error occured:",er)
            print(reply.errorString())


if __name__ == "__main__":
    app=QApplication(sys.argv)
    myHttp=MyHttp()
    myHttp._url='https://www.baidu.com'
    myHttp.request()
    sys.exit(app.exec_())
    
