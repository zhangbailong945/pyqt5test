from PyQt5.QtCore import QTimer,Qt,QDateTime,pyqtSignal
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,\
QListWidget,QLabel,QMessageBox,QPushButton
import sys

#内置信号和自定义槽函数

class SignalDemo1(QWidget):

    def __init__(self,parent=None):
        super(SignalDemo1,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        btnTest=QPushButton("关闭",self)
        btnTest.clicked.connect(self.showMsg)
    
    def showMsg(self):
        self.close()


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=SignalDemo1()
    demo.show()
    sys.exit(app.exec_())