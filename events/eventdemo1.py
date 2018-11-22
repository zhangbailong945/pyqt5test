from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal,QThread,QDateTime
import sys,time
from functools import partial
from PyQt5 import QtCore

'''
多线程
'''

class WinForm(QWidget):

    #通过类成员定义信号


    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setWindowTitle("pyqt5页面实时更新")
        self.resize(400,100)
        self.input=QLineEdit(self)
        self.input.resize(400,100)
        self.initUI()
    
    def initUI(self):
        #创建线程
        self.backend=BackendQThead()
        #连接信号
        self.backend.update_date_signal.connect(self.handleDisplay)
        #开始线程
        self.backend.start()
    
    #将当前时间输出到文本框
    def handleDisplay(self,text):
        self.input.setText(text)




class BackendQThead(QThread):
    #通过类成员对象定义信号
    update_date_signal=pyqtSignal(str)

    #处理业务逻辑
    def run(self):
        while True:
            data=QDateTime.currentDateTime()
            currtime=data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date_signal.emit(str(currtime))
            time.sleep(1)



if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())