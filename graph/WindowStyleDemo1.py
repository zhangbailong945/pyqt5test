from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        hlayout=QHBoxLayout()
        self.styleLabel=QLabel('Set Style:',self)
        self.styleComboBox=QComboBox(self)
        #从QStyleFactory显示多个样式
        self.styleComboBox.addItems(QStyleFactory.keys())
        #选择当前窗口风格
        index=self.styleComboBox.findText(
            QApplication.style().objectName(),
            QtCore.Qt.MatchFixedString
        )
        #设置风格 
        self.styleComboBox.setCurrentIndex(index)
        self.styleComboBox.activated[str].connect(self.handleStyleChanged)
        hlayout.addWidget(self.styleLabel)
        hlayout.addWidget(self.styleComboBox)
        self.setLayout(hlayout)
    
    def handleStyleChanged(self,style):
        QApplication.setStyle(style)





if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())