from PyQt5.QtWidgets import *
import sys

'''
内置信号和槽函数
内置信号：clicked
内置槽函数：close()
'''

class WinForm(QWidget):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()
    

    def initUI(self):
        self.setWindowTitle("内置信号和槽函数")
        self.resize(330,50)
        btn=QPushButton('关闭',self)
        btn.clicked.connect(self.close)

if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())