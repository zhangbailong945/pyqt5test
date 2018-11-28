

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time,os
import qdarkstyle


##不规则窗口

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setObjectName('myWindow')
        self.pix=QBitmap('d:/PyQt5Projects/pyqt5test/images/mask.png')
        self.resize(self.pix.size())
        self.setMask(self.pix)


    
    def paintEvent(self,envet):

        painter2=QPainter(self)
        painter2.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap('d:/PyQt5Projects/pyqt5test/images/python.jpg'))



if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())