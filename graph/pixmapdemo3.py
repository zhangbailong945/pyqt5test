from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time

##双缓冲技术，避免出现重影

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.pix=QPixmap()
        self.lastPoint=QPoint(600,500)
        self.endPoint=QPoint()
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
                #辅助画布
        self.temppix=QPixmap()
        #标志是否正在绘画
        self.isDrawing=False
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
        self.setWindowTitle("双缓冲绘图")
    
    def pixReset(self):
        self.pix.fill(Qt.white)
        self.update()
    
    def paintEvent(self,event):
        painter=QPainter(self)
        #根据鼠标指针前后两个位置绘制直线
        x=self.lastPoint.x()
        y=self.lastPoint.y()
        w=self.endPoint.x()-x
        h=self.endPoint.y()-y

        if self.isDrawing:
            self.temppix=self.pix
            pp=QPainter(self.temppix)
            pp.drawRect(x,y,w,h)
            painter.drawPixmap(0,0,self.temppix)
        else:
            pp=QPainter(self.pix)
            pp.drawRect(x,y,w,h)
            painter.drawPixmap(0,0,self.pix)

    
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.lastPoint=event.pos()
            self.endPoint=self.lastPoint
            self.isDrawing=True
    
    def mouseReleaseEvent(self,event):
        #释放鼠标左键
        if event.button()==Qt.LeftButton:
            self.endPoint==event.pos()
            #重绘
            self.update()
            self.isDrawing=False
    


if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())