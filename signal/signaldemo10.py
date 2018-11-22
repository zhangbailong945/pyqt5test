from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys
from functools import partial

'''
使用自定义参数
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
        btn1=QPushButton('button 1')
        btn2=QPushButton('button 2')
        
        #lambda表达式
        #btn1.clicked.connect(lambda:self.onButtonClick(1))
        #btn2.clicked.connect(lambda:self.onButtonClick(2))
        btn1.clicked.connect(partial(self.onButtonClick,1))
        btn2.clicked.connect(partial(self.onButtonClick,2))
        #偏函数

        layout=QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)
    
    def onButtonClick(self,n):
        print('button {0} 被按了下'.format(n))
        QMessageBox.information(self,'提示','Button {0} clicked!'.format(n))

if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())