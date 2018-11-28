

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time,os
import qdarkstyle


##設置窗口背景

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(600,500)
        self.setObjectName('myWindow')

        #使用QPalette設置窗口的背景色
        '''
        palette=QPalette()
        palette.setColor(QPalette.Background,Qt.red)
        self.setPalette(palette)
        '''

        #使用QPalette設置窗口的背景圖片
        '''
        palette=QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap('d:/PyQt5Projects/pyqt5test/images/python.jpg')))
        self.setPalette(palette)
        '''

    
    def paintEvent(self,envet):
        #使用paintEvent設置背景色
        '''
        painter=QPainter(self)
        painter.setBrush(Qt.black)
        #绘制矩形
        painter.drawRect(self.rect())
        '''

        '''
        painter1=QPainter(self)
        pixmap=QPixmap('d:/PyQt5Projects/pyqt5test/images/python.jpg')
        painter1.drawPixmap(self.rect(),pixmap)
        '''

        painter2=QPainter(self)
        painter2.drawPixmap(0,0,200,300,QPixmap('d:/PyQt5Projects/pyqt5test/images/python.jpg'))
        painter2.drawPixmap(200,0,200,300,QBitmap('d:/PyQt5Projects/pyqt5test/images/python.jpg'))



if __name__=="__main__":
    app=QApplication(sys.argv)
    qssStyle='''
      QWidget#myWindow{
          border-image:url(d:/PyQt5Projects/pyqt5test/images/python.jpg);
      }
      //QWidget#myWindow{
          //background-color:yellow;
      //}

    '''
    demo=WinForm()
    demo.setStyleSheet(qssStyle)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    #print(os.path.dirname(__file__))
    demo.show()
    sys.exit(app.exec_())