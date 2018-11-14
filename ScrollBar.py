import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow,QDockWidget,QTextEdit,QListWidget,\
QHBoxLayout,QScrollBar,QLabel,QWidget
from PyQt5.QtGui import QIcon,QPalette,QFont,QColor

class ScrollBarDemo(QWidget):

    def __init__(self,parent=None):
        super(ScrollBarDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        layout=QHBoxLayout()
        self.ltext=QLabel("拖动滑块改变颜色")
        self.ltext.setFont(QFont("Arial",16))
        layout.addWidget(self.ltext)
        self.s1=QScrollBar()
        self.s1.setMaximum(255)
        self.s1.sliderMoved.connect(self.sliderval)

        self.s2=QScrollBar()
        self.s2.setMaximum(255)
        self.s2.sliderMoved.connect(self.sliderval)

        self.s3=QScrollBar()
        self.s3.setMaximum(255)
        self.s3.sliderMoved.connect(self.sliderval)

        layout.addWidget(self.s1)
        layout.addWidget(self.s2)
        layout.addWidget(self.s3)

        self.setGeometry(300,300,300,200)
        self.setLayout(layout)
        self.setWindowTitle("QScrollBar 例子")
    
    def sliderval(self):
        palete=QPalette()
        c=QColor(self.s1.value(),self.s2.value(),self.s3.value())
        palete.setColor(QPalette.Foreground,c)
        self.ltext.setPalette(palete)

if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=ScrollBarDemo()
    demo.show()
    sys.exit(app.exec_())