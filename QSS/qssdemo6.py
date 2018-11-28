

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
        self.i=1
        self.mypix()
        self.timer=QTimer()
        self.timer.setInterval(500) #定时500毫秒刷新一次
        self.timer.timeout.connect(self.timeChange)
        self.timer.start()

    def mypix(self):
        self.update()
        if self.i==5:
            self.i=1
        
        self.mypic={
            1:'d:/PyQt5Projects/pyqt5test/images/left.png',
            2:'d:/PyQt5Projects/pyqt5test/images/up.png',
            3:'d:/PyQt5Projects/pyqt5test/images/right.png',
            4:'d:/PyQt5Projects/pyqt5test/images/down.png',
            }
        self.pix=QPixmap(self.mypic[self.i],"0",Qt.AvoidDither | Qt.ThresholdDither | Qt.ThresholdAlphaDither)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
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
        if event.button()==1:
            self.i+=1
            self.mypix()
    
    def timeChange(self):
        self.i+=1
        self.mypix()


if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())