from PyQt5.QtCore import QTimer,Qt,QDateTime,pyqtSignal
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QGridLayout,QListWidget,QLabel,\
QLCDNumber,QPushButton

import sys

global slice
sec=0





class TimerDemo(QWidget):

    def __init__(self,parent=None):
        super(TimerDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        layout=QVBoxLayout(self)
        #显示面板
        self.lcdNumber=QLCDNumber()
        layout.addWidget(self.lcdNumber)
        self.btnTest=QPushButton('测试')
        layout.addWidget(self.btnTest)
        self.timer=QTimer()
        self.timer.timeout.connect(self.setTime)
        self.btnTest.clicked.connect(self.work)


    def setTime(self):
        global sec
        sec+=1
        #LED显示数字+1
        self.lcdNumber.display(sec)
    
    def work(self):
        self.timer.start(1000)
        for i in range(20000000):
            pass
        
        self.timer.stop()






if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=TimerDemo()
    demo.show()
    sys.exit(app.exec_())