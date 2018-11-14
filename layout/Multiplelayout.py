from PyQt5.QtCore import QTimer,Qt,QDateTime
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QFormLayout,\
QHBoxLayout,QVBoxLayout,QPushButton,QHBoxLayout,QLabel,QLineEdit
import sys

##
#嵌套布局，只需要一个空白控件，然后在这个空白控件中进行多种布局
##

class MultiplelayoutDemo(QWidget):

    def __init__(self,parent=None):
        super(MultiplelayoutDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("嵌套布局例子")
        #嵌套布局
        self.resize(700,200)
        #全局控件
        wwg=QWidget(self)
        #全局布局
        wl=QHBoxLayout(wwg)
        #局部布局
        hlayout=QHBoxLayout()
        vlayout=QVBoxLayout()
        glayout=QGridLayout()
        formlayout=QFormLayout()

        hlayout.addWidget(QPushButton(str(1)))
        hlayout.addWidget(QPushButton(str(2)))

        vlayout.addWidget(QPushButton(str(3)))
        vlayout.addWidget(QPushButton(str(4)))

        glayout.addWidget(QPushButton(str(5)),0,0)
        glayout.addWidget(QPushButton(str(6)),0,1)

        glayout.addWidget(QPushButton(str(7)),1,0)
        glayout.addWidget(QPushButton(str(8)),1,1)

        formlayout.addRow(QLabel("测试1"),QLineEdit())
        formlayout.addRow(QLabel("测试2"),QLineEdit())
        formlayout.addRow(QLabel("测试3"),QLineEdit())
        formlayout.addRow(QLabel("测试4"),QLineEdit())

        #将局部布局添加到全局布局当中
        wl.addLayout(hlayout)
        wl.addLayout(vlayout)
        wl.addLayout(glayout)
        wl.addLayout(formlayout)

        #self.setLayout(layout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=MultiplelayoutDemo()
    demo.show()
    sys.exit(app.exec_())