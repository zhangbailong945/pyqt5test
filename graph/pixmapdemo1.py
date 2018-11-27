from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time

##简单绘图

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.pix=QPixmap()
        self.lastPoint=QPoint()
        self.endPoint=QPoint()
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.initUI()

    def initUI(self):
        self.resize(600,500)
        self.pix=QPixmap(600,400)
        self.pix.fill(Qt.white)
        self.labelImage=QLabel(self)
        #self.labelImage.resize(600,400)
        self.btnReSet=QPushButton('重新绘制')
        #self.labelImage.setStyleSheet("background-color:blue;")
        
        layout=QVBoxLayout()
        layout.addWidget(self.labelImage)
        layout.addWidget(self.btnReSet)
        self.setLayout(layout)
        self.btnReSet.clicked.connect(self.pixReset)
        self.setWindowTitle("简单绘图")
    
    def pixReset(self):
        self.pix.fill(Qt.white)
        self.update()
    
    def paintEvent(self,event):
        pp=QPainter(self.pix)
        #根据鼠标指针前后两个位置绘制直线
        pp.drawLine(self.lastPoint,self.endPoint)
        #让钱一个坐标等于后一个坐标的值，就能画出连续的线
        self.lastPoint=self.endPoint
        painer=QPainter(self)
        painer.drawPixmap(0,0,self.pix)
    
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.lastPoint=event.pos()
            self.endPoint=self.lastPoint
    
    def mouseMoveEvent(self,event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint=event.pos()
            #重新绘制
            self.update()
    
    def mouseReleaseEvent(self,event):
        #释放鼠标左键
        if event.button()==Qt.LeftButton:
            self.endPoint==event.pos()
            #重绘
            self.update()
    


if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())