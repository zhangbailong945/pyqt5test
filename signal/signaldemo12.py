from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal,QThread
import sys
from functools import partial
from PyQt5 import QtCore

'''
多线程
'''

class WinForm(QWidget):

    #自定义信号
    closeClicked=pyqtSignal()

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.qthread=MyThread()
        self.qthread.setIdentity("thread1")
        self.qthread.sinOut.connect(self.outText)
        self.qthread.setVal(6)
    
    def outText(self,text):
        print(text)



class MyThread(QThread):
    sinOut=pyqtSignal(str)

    def __init__(self,parent=None):
        super(MyThread,self).__init__(parent)
        self.identity=None
    
    def setIdentity(self,text):
        self.identity=text
    
    def setVal(self,val):
        self.times=int(val)
        #执行线程的run方法
        self.start()
    
    def run(self):
        while self.times>0 and self.identity:
            #发送信号
            self.sinOut.emit(self.identity+"==>"+str(self.times))
            self.times-=1


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())