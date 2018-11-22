from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal,QThread,QDateTime,QEvent,QTimer,Qt,QPoint
from PyQt5.QtGui import QPainter,QImage,QMouseEvent,QTransform,QPixmap
import sys,time
from functools import partial
from PyQt5 import QtCore

'''
事件处理
3.event过滤器
'''

class WinForm(QWidget):

    #通过类成员定义信号


    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setWindowTitle("event过滤器")
        self.width=600
        self.height=300

        self.label1=QLabel("请点击")
        self.label2=QLabel("请点击")
        self.label3=QLabel("请点击")
        self.labeState=QLabel("test")

        self.image1=QImage("D:\\PyQt5Projects\\pyqt5test\images\\test.ico")
        self.image2=QImage("D:\PyQt5Projects\pyqt5test\images\test.ico")
        self.image3=QImage("D:\PyQt5Projects\pyqt5test\images\test.ico")

        self.resize(self.width,self.height)

        #self.label1.installEventFilter(self)
        #self.label2.installEventFilter(self)
        #self.label3.installEventFilter(self)

        mainLayout=QGridLayout(self)
        mainLayout.addWidget(self.label1,500,0)
        mainLayout.addWidget(self.label2,500,1)
        mainLayout.addWidget(self.label3,500,2)
        mainLayout.addWidget(self.labeState,600,1)
        self.setLayout(mainLayout)
    
    def eventFilter(self,watched,event):
        #只对label1的点击事件进行过滤,重写其行为，其他事件会被忽略
        if watched==self.label1:
            if event.type()==QEvent.MouseButtonPress:
                mouseEvent=QMouseEvent(event)
                if mouseEvent.buttons()==Qt.LeftButton:
                    self.labeState.setText("按下鼠标左键")
                elif mouseEvent.buttons()==Qt.MidButton:
                    self.labeState.setText("按下鼠标中间")
                elif mouseEvent.buttons()==Qt.RightButton:
                    self.labeState.setText("按下鼠标右键")
                #转换图片大小
                transform=QTransform()
                transform.scale(0.5,0.5)
                tmp=self.image1.transformed(transform)
                self.label1.setPixmap(QPixmap(tmp))
            #鼠标释放事件
            if event.type()==QEvent.MouseButtonRelease:
                self.labeState.setText("释放鼠标按键")
                self.label1.setPixmap(QPixmap.fromImage(self.image1))
        #其他事件情况，返回默认事件处理方法
        return QWidget.eventFilter(self,watched,event)
    
 


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=WinForm()
    app.installEventFilter(demo)
    demo.show()
    sys.exit(app.exec_())