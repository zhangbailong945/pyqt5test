from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.resize(400,200)
        self.setWindowTitle("设置窗口的样式")
        #无边框设置
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:blue;")
    
    def showMaximized(self):
        #得到桌面控件
        desktop=QApplication.desktop()
        #得到屏幕可显示尺寸
        rect=desktop.availableGeometry()
        #设置窗口尺寸
        self.setGeometry(rect)
        self.show()


if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.showMaximized()
    sys.exit(app.exec_())