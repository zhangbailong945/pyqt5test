import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QColor,QCursor
from Libraries.Views.Ui_StatusBarWidget import Ui_StatusBarWidget


class Call_StatusBarWidget(QWidget,Ui_StatusBarWidget):

    def __init__(self,*args,**kwargs):
        super(Call_StatusBarWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        #
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(palette.Window, QColor(187,216, 234))
        self.setPalette(palette)
        #self.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.00568182, y1:0.051, x2:0, y2:0.563, stop:0 rgba(188, 217, 235, 255), stop:1 rgba(255, 255, 255, 255));background-color: rgb(192, 220, 239);")


    def enterEvent(self,event):
        super(Call_StatusBarWidget,self).enterEvent(event)
    
    def mousePressEvent(self,event):
        self.setCursor(QCursor(Qt.ArrowCursor))
        super(Call_StatusBarWidget,self).mousePressEvent(event)
    
    def mouseReleaseEvent(self,event):
        super(Call_StatusBarWidget,self).mouseReleaseEvent(event)
    
    def mouseMoveEvent(self,event):
        self.setCursor(QCursor(Qt.ArrowCursor))
        super(Call_StatusBarWidget,self).mouseMoveEvent(event)