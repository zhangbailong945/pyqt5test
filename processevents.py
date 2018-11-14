from PyQt5.QtCore import QTimer,Qt,QDateTime
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QListWidget,QLabel,QPushButton
import sys,time


class TimerDemo(QWidget):

    def __init__(self,parent=None):
        super(TimerDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.listFile=QListWidget()
        self.btnStart=QPushButton("开始")
        layout=QGridLayout(self)
        layout.addWidget(self.listFile,0,0,1,2)
        layout.addWidget(self.btnStart,1,1)
        self.btnStart.clicked.connect(self.slotAdd)
        self.setLayout(layout)
    
    def slotAdd(self):
        for n in range(10):
            str_n='File Index{0}'.format(n)
            self.listFile.addItem(str_n)
            QApplication.processEvents()
            time.sleep(1)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=TimerDemo()
    demo.show()
    sys.exit(app.exec_())