from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys

'''
自定义信号和槽函数
自定义信号：closeClicked
槽函数：close()
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
        btn=QPushButton('关闭',self)
        #连接信号与槽函数
        btn.clicked.connect(self.btn_clicked)
        #接受信号，连接到自定义槽函数
        self.closeClicked.connect(self.btn_close)
    
    def btn_clicked(self):
        #发送自定义信号，无参数
        self.closeClicked.emit()

    #自定义槽函数
    def btn_close(self):
        self.close()

if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())