from PyQt5.QtCore import QTimer,Qt,QDateTime
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QFormLayout,\
QHBoxLayout,QVBoxLayout,QPushButton,QHBoxLayout,QLabel,QLineEdit,QTextEdit
import sys

##
#网格布局
##

class GridlaoutDemo(QWidget):

    def __init__(self,parent=None):
        super(GridlaoutDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Hboxlayout 跨列、跨行例子")
        layout=QFormLayout()
        layout.addRow(QLabel("姓名"),QLineEdit())
        layout.addRow(QLabel("年龄"),QLineEdit())
        layout.addRow(QLabel("其他"),QLineEdit())
        self.setWindowTitle("Formlayout")

        self.setLayout(layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=GridlaoutDemo()
    demo.show()
    sys.exit(app.exec_())