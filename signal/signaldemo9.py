from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys

'''
综合实例
'''

class WinForm(QWidget):

    #自定义信号
    #无参数
    signal1=pyqtSignal()

    #int参数
    signal2=pyqtSignal(int)

    #int和str参数
    signal3=pyqtSignal(int,str)

    #list参数
    signal4=pyqtSignal(list)

    #dict参数
    signal5=pyqtSignal(dict)
    
    #重载参数
    signal6=pyqtSignal([int,str],[str])




    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()
    

    def initUI(self):
        self.setWindowTitle("自定义信号和内置槽函数")
        self.resize(330,50)
        btn=QPushButton('关闭',self)
        #连接信号与槽函数
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        self.signal6[int,str].connect(self.signalCall6Overload)
        self.signal6[str].connect(self.signalCall6Overload)

        #发射信号
        self.signal1.emit()
        self.signal2.emit(1)
        self.signal3.emit(1,'loach')
        self.signal4.emit([1,2,3,4])
        self.signal5.emit({"name":'zhangsan','age':'25'})
        self.signal6[int,str].emit(1,'loach')
        self.signal6[str].emit('loach')
    
    def signalCall1(self):
        print('signal1 emit')
    
    def signalCall2(self,val):
        print('signal1 emit,value:',val)
    
    def signalCall3(self,val,text):
        print('signal1 emit,value:',val,text)
    
    def signalCall4(self,val):
        print('signal1 emit,value:',val)
    
    def signalCall5(self,val):
        print('signal1 emit,value:',val)
    
    def signalCall6(self,val,text):
        print('signal1 emit,value:',val,text)
    
    def signalCall6Overload(self,text):
        print('signal1 emit,value',text)

if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())