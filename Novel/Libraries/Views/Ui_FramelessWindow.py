import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout
from PyQt5.QtGui import QPainter,QPen,QColor
#标题栏窗口
from Libraries.Controls.Call_TitleBarWidget import Call_TitleBarWidget
#状态栏窗口
from Libraries.Controls.Call_StatusBarWidget import Call_StatusBarWidget

class FramelessWindow(QWidget):

    #四周边距
    Margins=5

    def __init__(self,*args,**kwargs):
        super(FramelessWindow,self).__init__(*args,**kwargs)
        self._pressed=False
        self.Direction=None
        self._mPos=None
        #背景透明
        self.setAttribute(Qt.WA_TranslucentBackground,True)
        #无边框
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        #鼠标跟踪
        self.setMouseTracking(True)
        #布局
        #垂直布局 头部标题栏 中部QWidget 底部 状态栏
        layout=QVBoxLayout(self,spacing=0)
        #预留边界用于实现无边框窗口调整大小
        layout.setContentsMargins(self.Margins,self.Margins,self.Margins,self.Margins)
        #标题栏
        self.titleBar=Call_TitleBarWidget(self)
        layout.addWidget(self.titleBar)
        self.contentWidget=QWidget(self)
        self.contentWidget.resize(950,300)
        self.contentWidget.setStyleSheet("background-color:white;")
        layout.addWidget(self.contentWidget)
        self.statusBar=Call_StatusBarWidget(self)
        self.statusBar.setStyleSheet("background-color:white;")
        layout.addWidget(self.statusBar)
    
    def paintEvent(self,event):
        super(FramelessWindow,self).paintEvent(event)
        painter=QPainter(self)
        painter.setPen(QPen(QColor(255,255,255,1),2*self.Margins))
        painter.drawRect(self.rect())

    def mousePressEvent(self,event):
        super(FramelessWindow,self).mousePressEvent(event)
        if event.button()==Qt.LeftButton:
            self._mPos=event.pos()
    
    def mouseReleaseEvent(self,event):
        super(FramelessWindow,self).mouseReleaseEvent(event)
        self._pressed=False
        self.Direction=None

    def mouseMoveEvent(self,event):
        super(FramelessWindow,self).mouseMoveEvent(event)
        pos=event.pos()
        xPos,yPos=pos.x(),pos.y()
        wm,hm=self.width()-self.Margins,self.height()-self.Margins

        if event.buttons()==Qt.LeftButton and self._pressed:
            self._resizeWidget(pos)
            return
    
    def _resizeWidget(self,pos):
        """调整窗口大小"""
        if self.Direction == None:
            return
        mpos = pos - self._mpos
        xPos, yPos = mpos.x(), mpos.y()
        geometry = self.geometry()
        x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
        self.setGeometry(x,y,w,h)

