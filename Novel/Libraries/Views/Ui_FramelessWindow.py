import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout
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
        

