from PyQt5.QtCore import QTimer,Qt,QDateTime
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton,QHBoxLayout
import sys


class HboxLayoutDemo(QWidget):

    def __init__(self,parent=None):
        super(HboxLayoutDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Hboxlayout例子")
        #水平布局
        layout=QHBoxLayout()
        layout.addWidget(QPushButton(str(1)))
        layout.addWidget(QPushButton(str(2)),0,Qt.AlignTop)
        layout.addWidget(QPushButton(str(3)),0,Qt.AlignLeft|Qt.AlignTop)
        layout.addWidget(QPushButton(str(4)),0,Qt.AlignLeft|Qt.AlignBottom)
        layout.addWidget(QPushButton(str(5)),0,Qt.AlignLeft|Qt.AlignBottom)
        #设置布局中控件之间的距离
        layout.setSpacing(0)
        self.setLayout(layout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=HboxLayoutDemo()
    demo.show()
    sys.exit(app.exec_())