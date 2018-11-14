from PyQt5.QtCore import QTimer,Qt,QDateTime
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QHBoxLayout
import sys

##
#垂直布局
##

class VboxLayoutDemo(QWidget):

    def __init__(self,parent=None):
        super(VboxLayoutDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Hboxlayout例子")
        #水平布局
        layout=QVBoxLayout()
        layout.addWidget(QPushButton(str(1)))
        #添加伸缩量
        layout.addStretch(1)
        layout.addWidget(QPushButton(str(2)))
        layout.addStretch(1)
        layout.addWidget(QPushButton(str(3)))
        layout.addStretch(1)
        layout.addWidget(QPushButton(str(4)))
        layout.addStretch(1)
        layout.addWidget(QPushButton(str(5)))
        #设置布局中控件之间的距离
        layout.setSpacing(0)
        self.setLayout(layout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=VboxLayoutDemo()
    demo.show()
    sys.exit(app.exec_())