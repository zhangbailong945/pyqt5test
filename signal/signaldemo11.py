from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys
from functools import partial
from PyQt5 import QtCore

'''
装饰器信号与槽函数
'''

class WinForm(QWidget):

    #自定义信号
    closeClicked=pyqtSignal()

    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()
    

    def initUI(self):
        self.setWindowTitle("自定义信号和内置槽函数")
        self.resize(330,50)
        self.btn1=QPushButton('button 1')
        #设置对象
        self.btn1.setObjectName("okButton")
        layout=QHBoxLayout()
        layout.addWidget(self.btn1)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.btn1.clicked.connect(self.okButton_clicked)

    
    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print('button 1被按了下')
        self.btn1.disconnect()
    
    def okButton_clicked(self):
        print("button 1 被按了下")
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())