from PyQt5.QtCore import QTimer,Qt,QDateTime,QUrl
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QListWidget,QLabel,\
QVBoxLayout,QHBoxLayout
from PyQt5.QtWebEngineWidgets import *
import sys

#嵌入html5代码


class TimerDemo(QWidget):

    def __init__(self,parent=None):
        super(TimerDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        layout=QVBoxLayout()
        self.browser=QWebEngineView()
        url="http://www.baidu.com"
        html="""
        <html>
        <head>
        <title>PyQt5嵌入html5</title>
        </head>
        <body>
        <h1>Hello PyQt5!</h1>
        <h1>Hello PyQt5!</h1>
        <h1>Hello PyQt5!</h1>
        <h1>Hello PyQt5!</h1>
        <h1>Hello PyQt5!</h1>
        </body>
        </html>
        """
        self.browser.setHtml(html)
        layout.addWidget(self.browser)
        self.setLayout(layout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=TimerDemo()
    demo.show()
    sys.exit(app.exec_())