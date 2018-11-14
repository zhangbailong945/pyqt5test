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
        title=QLabel("标题")
        author=QLabel('提交人')
        review=QLabel("申告报告")

        titleEdit=QLineEdit()
        authorEdit=QLineEdit()
        reviewEdit=QTextEdit()

        layout=QGridLayout()
        layout.setSpacing(10)
        layout.addWidget(title,1,0)
        layout.addWidget(titleEdit,1,1)
        layout.addWidget(author,2,0)
        layout.addWidget(authorEdit,2,1)
        layout.addWidget(review,3,0)
        layout.addWidget(reviewEdit,3,1,5,1)
        self.setGeometry(300,300,300,400)
        self.setWindowTitle("Gridlayout 跨列 跨行")

        self.setLayout(layout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=GridlaoutDemo()
    demo.show()
    sys.exit(app.exec_())