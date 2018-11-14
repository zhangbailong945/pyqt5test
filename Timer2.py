from PyQt5.QtCore import QTimer,Qt,QDateTime
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QListWidget,QLabel
import sys


class TimerDemo(QWidget):

    def __init__(self,parent=None):
        super(TimerDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        layout=QVBoxLayout()
        label=QLabel("<font color=red size=18><b>Hello PyQt5,窗口会在10秒内小时！</b></font>")
        layout.addWidget(label)
        self.setLayout(layout)
        self.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
        self.resize(300,24)
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=TimerDemo()
    demo.show()
    QTimer.singleShot(10000,app.quit)
    sys.exit(app.exec_())