from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal,QThread,QDateTime,Qt
import sys,time
from functools import partial
from PyQt5 import QtCore

'''
单一窗口数据传递
'''

class WinForm(QWidget):

    #通过类成员定义信号


    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setWindowTitle("单个窗口数据传递")
        self.initUI()
    
    def initUI(self):
        #创建滑块和LCD控件
        self.lcd=QLCDNumber()
        self.slider=QSlider(Qt.Horizontal)

        vobx=QVBoxLayout()
        vobx.addWidget(self.lcd)
        vobx.addWidget(self.slider)

        self.setLayout(vobx)

        self.slider.valueChanged.connect(self.lcd.display)

        self.setGeometry(300,300,350,150)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())