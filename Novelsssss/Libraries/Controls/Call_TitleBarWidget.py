import sys

from PyQt5.QtCore import Qt,pyqtSignal,QPoint
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QColor,QCursor
from Libraries.Views.Ui_TitleBarWidget import Ui_TitleBarWidget



class Call_TitleBarWidget(QWidget,Ui_TitleBarWidget):
    
    # 窗口移动
    windowMoved = pyqtSignal(QPoint)
    #窗口最小化
    windowMinimumed=pyqtSignal()
    #窗口最大化
    windowMaximumed=pyqtSignal()
    #窗口还原
    windowNormaled=pyqtSignal()
    #窗口关闭
    windowClosed=pyqtSignal()
    #窗口设置
    windowSetting=pyqtSignal()

    def __init__(self,*args,**kwargs):
        super(Call_TitleBarWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        #允许QSS设置背景色
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(palette.Window, QColor(187,216, 234))
        self.setPalette(palette)
        

        

    def enterEvent(self,event):
        super(Call_TitleBarWidget,self).enterEvent(event)
    
    def mousePressEvent(self,event):
        self.setCursor(QCursor(Qt.ArrowCursor))
        super(Call_TitleBarWidget,self).mousePressEvent(event)
    
    def mouseReleaseEvent(self,event):
        super(Call_TitleBarWidget,self).mouseReleaseEvent(event)
    
    def mouseMoveEvent(self,event):
        self.setCursor(QCursor(Qt.ArrowCursor))
        super(Call_TitleBarWidget,self).mouseMoveEvent(event)


