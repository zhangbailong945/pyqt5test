

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time,os
import qdarkstyle


##不规则窗口实现动画效果

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.label1=QLabel('',self)
        self.setFixedSize(128,128)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.moive=QMovie("d:/PyQt5Projects/pyqt5test/images/loading.gif")
        self.label1.setMovie(self.moive)
        self.moive.start()
        self.setWindowOpacity(0.5)


if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())