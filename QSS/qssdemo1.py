from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time

##QSS的UI美化

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
        self.btn1=QPushButton('test')
        self.btnReSet=QPushButton('重新绘制') 
        self.btn2=QPushButton('test2')
        self.btn2.setProperty('name','mybtn')
        layout=QVBoxLayout()
        layout.addWidget(self.btnReSet)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        self.setLayout(layout)
        self.setWindowTitle("QSS美化")


if __name__=="__main__":
    app=QApplication(sys.argv)
    qssStyle='''
      QPushButton{
          background-color:red;
      }

      QPushButton[name='mybtn']{
          background-color:blue;
      }
    '''
    demo=WinForm()
    demo.setStyleSheet(qssStyle)
    demo.show()
    sys.exit(app.exec_())