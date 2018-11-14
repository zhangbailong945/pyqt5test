from PyQt5.QtCore import QTimer,Qt,QDateTime,QUrl,pyqtProperty
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QListWidget,QLabel,\
QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import QWebChannel
from MySharedObject import MySharedObject

import sys

#嵌入javascript ,pyqt5与javascript交互


class TimerDemo(QWidget):

    def __init__(self,parent=None):
        super(TimerDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        layout=QVBoxLayout()
        self.browser=QWebEngineView()
        self.browser.load(QUrl('index.html'))

        #创建共享对象
        channel=QWebChannel()
        myobj=MySharedObject()
        channel.registerObject("bridge",myobj)
        self.browser.page().setWebChannel(channel)
        

        

        layout.addWidget(self.browser)
        self.setLayout(layout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=TimerDemo()
    demo.show()
    sys.exit(app.exec_())