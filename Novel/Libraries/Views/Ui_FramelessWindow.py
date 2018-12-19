import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout
from PyQt5.QtGui import QPainter,QPen,QColor,QCursor
#标题栏窗口
from Libraries.Controls.Call_TitleBarWidget import Call_TitleBarWidget
#状态栏窗口
from Libraries.Controls.Call_StatusBarWidget import Call_StatusBarWidget
#默认的QSS
from Libraries.Qss.Default import Default

class FramelessWindow(QWidget):

    #四周边距
    Margins=5

    def __init__(self,*args,**kwargs):
        super(FramelessWindow,self).__init__(*args,**kwargs)
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
        layout.addWidget(self.statusBar)

        self.setStyleSheet(Default.DEFAULT_QSS)

        #隐藏到任务栏，内置信号触发自定义函数
        self.titleBar.min_btn.clicked.connect(self.showMinimized_Call)
        #之定义信号触发内置函数
        self.titleBar.windowMinimumed.connect(self.showMinimized)
        #关闭按钮内置单击信号，触发自定义函数
        self.titleBar.close_btn.clicked.connect(self.close_Call)
        #自定义信号触发内置函数
        self.titleBar.windowClosed.connect(self.close)

        self.titleBar.max_btn.clicked.connect(self.showMaxed)
        self.titleBar.windowMaximumed.connect(self.showMax)
        self.titleBar.windowNormaled.connect(self.showNormal)
    
    def showMax(self):
        self.showMaximized()
        self.layout().setContentsMargins(0,0,0,0)
    
    def showNormal(self):
        super(FramelessWindow, self).showNormal()
        self.layout().setContentsMargins(self.Margins,self.Margins,self.Margins,self.Margins)
    
    def showMaxed(self):
        if self.titleBar.max_btn.text()=='口':
            #最大化
            self.titleBar.max_btn.setText("回")
            self.titleBar.windowMaximumed.emit()
        else:
            self.titleBar.max_btn.setText("口")
            self.titleBar.windowNormaled.emit()
    
    #触发隐藏到任务栏信号
    def showMinimized_Call(self):
        #绑定事件
        self.titleBar.windowMinimumed.emit()
    #触发关闭app信号
    def close_Call(self):
        self.titleBar.windowClosed.emit()
    
    def paintEvent(self,event):
        super(FramelessWindow,self).paintEvent(event)
        painter=QPainter(self)
        painter.setPen(QPen(QColor(255,255,255,1),2*self.Margins))
        painter.drawRect(self.rect())

    #鼠标按下
    def mousePressEvent(self,event):
        super(FramelessWindow,self).mousePressEvent(event)
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.SizeAllCursor))
    #鼠标释放
    def mouseReleaseEvent(self,event):
        super(FramelessWindow,self).mouseReleaseEvent(event)
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    #鼠标移动
    def mouseMoveEvent(self,event):
        super(FramelessWindow,self).mouseMoveEvent(event)
        if event.buttons()==Qt.LeftButton and self.m_drag:
            self.move(event.globalPos()-self.m_DragPosition)
            event.accept()

