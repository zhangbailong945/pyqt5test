from PyQt5.QtCore import QTimer,Qt,QDateTime
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QFormLayout,QHBoxLayout,QVBoxLayout,QPushButton,QHBoxLayout
import sys

##
#网格布局
##

class GridlaoutDemo(QWidget):

    def __init__(self,parent=None):
        super(GridlaoutDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Hboxlayout例子")
        #水平布局
        layout=QGridLayout()
        names=[
            'Cls','Back','','Close',
            '7','8','9','/',
            '4','5','6','*',
            '0','.','=','+'
        ]
        positions=[(i,j) for i in range(5) for j in range(4)]
        for positions,name in zip(positions,names):
            if name=='':
                continue
            button=QPushButton(name)
            layout.addWidget(button,*positions)
        self.move(300,150)
        self.setLayout(layout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=GridlaoutDemo()
    demo.show()
    sys.exit(app.exec_())