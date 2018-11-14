from PyQt5.QtCore import QTimer,Qt,QDateTime,QUrl
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QListWidget,QLabel,\
QVBoxLayout,QHBoxLayout
from PyQt5.QtWebEngineWidgets import *
import sys


class TimerDemo(QWidget):

    def __init__(self,parent=None):
        super(TimerDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        layout=QVBoxLayout()
        self.browser=QWebEngineView()
        url="http://www.baidu.com"
        self.browser.load(QUrl(url))
        layout.addWidget(self.browser)
        self.setLayout(layout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=TimerDemo()
    demo.show()
    sys.exit(app.exec_())