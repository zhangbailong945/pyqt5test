from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal,QThread,QDateTime,QEvent,QTimer,Qt,QPoint
from PyQt5.QtGui import QPainter
import sys,time
from functools import partial
from PyQt5 import QtCore

'''
事件处理
1.重新实现事件函数
2.重载event函数
'''

class WinForm(QWidget):

    #通过类成员定义信号


    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setWindowTitle("重新实现事件函数")
        self.resize(400,300)
        self.justDoubleClicked=False
        self.key=""
        self.text=""
        self.message=""
        self.move(100,100)
        #避免受到窗口大小重绘事件的影响，可以把参数0改成3000(秒)，然后在运行
        QTimer.singleShot(3000,self.giveHelp)
    
    def giveHelp(self):
        #创建线程
        self.text="请点击这里出发追踪鼠标功能"
        #重绘事件，触发paintEvent函数
        self.update()
    
    def closeEvent(self,event):
        print("Closed")
    
    def contextMenuEvent(self,event):
        menu=QMenu(self)
        oneAction=menu.addAction("&One")
        towAction=menu.addAction("&Two")
        oneAction.triggered.connect(self.one)
        towAction.triggered.connect(self.two)
        if not self.message:
            menu.addSeparator()
            threeAction=menu.addAction("&Three")
            threeAction.triggered.connect(self.three)
        menu.exec_(event.globalPos())
    
    ##上下文菜单槽
    def one(self):
        self.message="Menu option one"
        self.update()
    
    def two(self):
        self.message="Menu option two"
        self.update()

    def three(self):
        self.message="Menu option three"
        self.update()
    
    #重新实现绘制事件
    def paintEvent(self,event):
        text=self.text
        i=text.find("\n\n")
        if i>=0:
            text=text[0:i]
        #如果触发了键盘上按键，则在文本上显示这个按键
        if self.key:
            text+="\n\n你刚刚按了{0} 键.".format(self.key)
        painter=QPainter(self)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.drawText(self.rect(),Qt.AlignCenter,text)
        if self.message:
            painter.drawText(self.rect(),Qt.AlignBottom|Qt.AlignCenter,self.message)
            QTimer.singleShot(5000,self.clearMessage)
            QTimer.singleShot(5000,self.update)
    
    def clearMessage(self):
        self.message=""
    
    #重现实现窗口大小事件
    def resizeEvent(self,event):
        self.text="调整窗口大小:QSize({0},{1})".format(event.size().width(),event.size().height())
        self.update()
    
    #重新实现鼠标释放事件
    def mouseReleaseEvent(self,event):
        if self.justDoubleClicked:
            self.justDoubleClicked=False
        else:
            #单击鼠标
            self.setMouseTracking(not self.hasMouseTracking())
            if self.hasMouseTracking():
                self.text="开启鼠标跟踪功能.\n"+\
                "请移动一下鼠标!\n"+\
                "单击鼠标可以关闭这个功能"
            else:
                self.text="关闭鼠标跟踪功能\n"+\
                "单击鼠标可以开启这个功能"
            self.update()
    
    def mouseMoveEvent(self,event):
        if not self.justDoubleClicked:
            #将窗口坐标转换为屏幕坐标
            globalPos=self.mapToGlobal(event.pos())
            self.text="""
            鼠标位置：
            窗口坐标：QPint({0},{1})
            屏幕坐标：QPint({2},{3})
            """.format(event.pos().x(),event.pos().y(),globalPos.x(),globalPos.y())
            self.update()
    
    def mouseDoubleClickEvent(self,event):
        self.justDoubleClicked=True
        self.text="你双击了鼠标"
        self.update()
    
    def keyPressEvent(self,event):
        self.key=""
        if event.key()==Qt.Key_Home:
            self.key="home key press!"
        elif event.key()==Qt.Key_End:
            self.key="End key press!"
        elif event.key()==Qt.Key_PageUp:
            if event.modifiers() & Qt.ControlModifier:
                self.key="Ctrl + PageDown press!"
            else:
                self.key="PageDown key press!"
        elif Qt.Key_A<=event.key()<=Qt.Key_Z:
            if event.modifiers() & Qt.ShiftModifier:
                self.key="Shift + "
            self.key+=event.text()
        if self.key:
            self.key=self.key
            self.update()
        else:
            QWidget.keyPressEvent(self,event)
    
    #重载event函数
    def event(self,event):
        if (event.type()==QEvent.KeyPress and event.key()==Qt.Key_Tab):
            self.key="在event()中捕获Tab key!"
            self.update()
            return True
        return QWidget.event(self,event)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())