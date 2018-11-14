from PyQt5.QtCore import QTimer,Qt,QDateTime
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
import sys


class AbsoluteDemo(QWidget):

    def __init__(self,parent=None):
        super(AbsoluteDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        label1=QLabel('第一个标签',self)
        label1.move(15,10)
        label2=QLabel('第二个标签',self)
        label2.move(35,40)
        label3=QLabel('第三个标签',self)
        label3.move(55,70)
        self.setGeometry(300,300,320,120)
        self.setWindowTitle("绝对位置布局")



if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=AbsoluteDemo()
    demo.show()
    sys.exit(app.exec_())