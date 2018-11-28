

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time,os
import qdarkstyle
from CommonHelper import CommonHelpler


##换皮肤功能

class WinForm(QMainWindow):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.resize(400,400)
        self.setObjectName('myWidget')


if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    styleFile='d:/PyQt5Projects/pyqt5test/qss/default.qss'
    style=CommonHelpler.readQss(styleFile)
    demo.setStyleSheet(style)
    demo.show()
    sys.exit(app.exec_())