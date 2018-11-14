from PyQt5.QtCore import QTimer,Qt,QDateTime,pyqtSignal
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,\
QListWidget,QLabel,QMessageBox,QPushButton
import sys


class SignalDemo1(QWidget):

    def __init__(self,parent=None):
        super(SignalDemo1,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        btnTest=QPushButton("测试",self)
        btnTest.clicked.connect(self.showMsg)
    
    def showMsg(self):
        QMessageBox.information(self,"提示","弹出测试信息")


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=SignalDemo1()
    demo.show()
    sys.exit(app.exec_())