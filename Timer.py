from PyQt5.QtCore import QTimer,Qt,QDateTime
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QListWidget,QLabel,QPushButton
import sys


class TimerDemo(QWidget):

    def __init__(self,parent=None):
        super(TimerDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.listFile=QListWidget()
        self.label1=QLabel("显示当前时间")
        self.startBtn=QPushButton('开始')
        self.endBtn=QPushButton('结束')

        layout=QGridLayout(self)
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.showTimer)

        layout.addWidget(self.label1,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.setLayout(layout)
    

    def showTimer(self):
        time=QDateTime.currentDateTime()
        timeDisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label1.setText(timeDisplay)
    
    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)
    
    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)



if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=TimerDemo()
    demo.show()
    sys.exit(app.exec_())