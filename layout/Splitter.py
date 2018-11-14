from PyQt5.QtCore import QTimer,Qt,QDateTime
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QFormLayout,\
QHBoxLayout,QVBoxLayout,QPushButton,QHBoxLayout,QLabel,QLineEdit,QSplitter,QFrame,\
QTextEdit
import sys

##
#嵌套布局，只需要一个空白控件，然后在这个空白控件中进行多种布局
##

class SplitterlayoutDemo(QWidget):

    def __init__(self,parent=None):
        super(SplitterlayoutDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("QSplitter")
        layout=QHBoxLayout(self)
        self.setGeometry(300,300,300,200)
        topLeft=QFrame()
        topLeft.setFrameShape(QFrame.StyledPanel)
        buttom=QFrame()
        buttom.setFrameShape(QFrame.StyledPanel)
        splitter1=QSplitter(Qt.Horizontal)
        textEdit1=QTextEdit()
        splitter1.addWidget(topLeft)
        splitter1.addWidget(textEdit1)
        splitter1.setSizes([100,200])
        splitter2=QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(buttom)
        layout.addWidget(splitter2)
        self.setLayout(layout)




if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=SplitterlayoutDemo()
    demo.show()
    sys.exit(app.exec_())