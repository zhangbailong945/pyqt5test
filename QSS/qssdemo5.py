

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time,os
import qdarkstyle


##拖动不规则窗口

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.mypix()

    def mypix(self):
        self.mypic='d:/PyQt5Projects/pyqt5test/images/mask.png'
        self.mainpic='d:/PyQt5Projects/pyqt5test/images/python.png'
        self.pix=QBitmap(self.mypic)
        self.resize(self.pix.size())
        self.setMask(self.pix)
        self.dragPosition=None


    #重载鼠标按下函数
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_dragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

        if event.button()==Qt.RightButton:
            self.close()
    
    #重载鼠标移动函数
    def mouseMoveEvent(self,QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_dragPosition)
            QMouseEvent.accept()
    
    #鼠标释放
    def mouseReleaseEvent(self,event):
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    


    def paintEvent(self,envet):
        painter=QPainter(self)
        painter.drawPixmap(
            0,
            0,
            self.pix.width(),
            self.pix.height(),
            self.pix
        )
    
    def mouseDoubleClickEvent(self,event):
        self.mypix()


if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())