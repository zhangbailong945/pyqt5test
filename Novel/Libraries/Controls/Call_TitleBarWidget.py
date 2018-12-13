import sys

from PyQt5.QtCore import Qt,pyqtSignal,QPoint
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QColor
from Libraries.Views.Ui_TitleBarWidget import Ui_TitleBarWidget


class Call_TitleBarWidget(QWidget,Ui_TitleBarWidget):
    
    # 窗口移动
    windowMoved = pyqtSignal(QPoint)

    def __init__(self,*args,**kwargs):
        super(Call_TitleBarWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.mPos=None
        #
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(palette.Window, QColor(187,216, 234))
        self.setPalette(palette)
    

    def enterEvent(self,event):
        self.setCursor(Qt.ArrowCursor)
        super(Call_TitleBarWidget,self).enterEvent(event)
    
    def mousePressEvent(self,event):
        #
        if event.button()==Qt.LeftButton:
            self.mPos=event.pos()
        event.accept()
    
    def mouseReleaseEvent(self,event):
        self.mPos=None
        event.accept()
    
    def mouseMoveEvent(self,event):
        if event.buttons()==Qt.LeftButton and self.mPos:
            self.windowMoved.emit(self.mapToGlobal(event.pos()-self.mPos))
        event.accept()


