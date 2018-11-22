from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys

'''
信号与槽高级玩法
'''

class WinForm(QWidget):

    #无参数的信号
    signal_NoParameter=pyqtSignal()
    #一个参数的信号
    signal_OneParmeter=pyqtSignal(int)
    #但一个参数（整数或者字符串）的重载版本的信号
    signal_OneParmeter_Overload=pyqtSignal([int],[str])
    #带两个参数(整数或字符串)的信号
    signal_TwoParmeter=pyqtSignal(int,str)
    #带两个参数(整数，整数和整数或字符串)的信号重载版本的信号
    signal_TwoParmeter_Overload=pyqtSignal([int,int],[int,str])



    def __init__(self,parent=None):
        super().__init__(parent)
        #连接信号与槽
        self.signal_NoParameter.connect(self.setValue_NoParameter)
        self.signal_OneParmeter.connect(self.setValue_NoParameter)
        self.signal_OneParmeter_Overload.connect(self.setValue_NoParameter)
        self.signal_TwoParmeter(self.setValue_NoParameter)
        self.signal_TwoParmeter_Overload(self.setValue_NoParameter)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("自定义信号和内置槽函数")
        self.resize(330,50)
        btn=QPushButton('关闭',self)
    
    #无参数的槽函数
    def setValue_NoParameter(self):
        pass
    #带一个参数的槽函数（整数）
    def setValue_NoParameter(self,nIndex):
        pass
    #带一个参数的槽函数（字符串）
    def setValue_NoParameter(self,sIndex):
        pass
    #带两个参数的槽函数（整数，整数）
    def setValue_NoParameter(self,x,y):
        pass
    #带两个参数的槽函数（整数，字符串）
    def setValue_NoParameter(self,x,stry):
        pass
    

    ##信号的发射
    def mousePressEvent(self,event):
        #发射无参数的信号
        self.signal_NoParameter.emit()
        #带一个参数的信号
        self.signal_OneParmeter.emit(1)
        #发射带一个参数的重载版本的信号
        self.signal_OneParmeter_Overload.emit(1)
        #发射带两个参数的信号
        self.signal_TwoParmeter.emit(1,'abc')
        #发射带两个参数的信号的重载版本
        self.signal_TwoParmeter_Overload.emit(1,2)    

if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())